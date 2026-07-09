#!/usr/bin/env python3
"""Validate manuals repo: every PDF has a matching markdown conversion."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANUAL_MD_TAG = "# format=manual-md"
WEB_MD_TAG = "# format=web-source-md"
MACHINE_MANIFEST_TAG = "# format=machine-manifest"


def machine_dirs(root: Path) -> list[Path]:
    skip = {"tools", ".github", ".git", ".cursor"}
    return sorted(
        p for p in root.iterdir() if p.is_dir() and p.name not in skip and not p.name.startswith(".")
    )


def find_pdfs(root: Path) -> list[Path]:
    pdfs: list[Path] = []
    for machine in machine_dirs(root):
        pdfs.extend(sorted(machine.glob("*.pdf")))
    return pdfs


def validate_manual_md(md_path: Path, pdf_name: str) -> list[str]:
    errors: list[str] = []
    if not md_path.is_file():
        errors.append(f"missing markdown for {pdf_name}: expected {md_path.name}")
        return errors

    text = md_path.read_text(encoding="utf-8")
    if not text.startswith(MANUAL_MD_TAG):
        errors.append(f"{md_path}: must start with {MANUAL_MD_TAG!r}")

    if f"source_pdf: {pdf_name}" not in text:
        errors.append(f"{md_path}: header must include source_pdf: {pdf_name}")

    pages = re.findall(r"^## Page (\d+)$", text, re.MULTILINE)
    if not pages:
        errors.append(f"{md_path}: no ## Page N headings found")

    return errors


def validate_web_md(md_path: Path) -> list[str]:
    errors: list[str] = []
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith(WEB_MD_TAG):
        errors.append(f"{md_path}: must start with {WEB_MD_TAG!r}")
    if "source_url:" not in text.split("---", 1)[0]:
        errors.append(f"{md_path}: header must include source_url:")
    return errors


def validate_manifest(manifest_path: Path) -> list[str]:
    errors: list[str] = []
    if not manifest_path.is_file():
        return errors

    text = manifest_path.read_text(encoding="utf-8")
    if not text.startswith(MACHINE_MANIFEST_TAG):
        errors.append(f"{manifest_path}: must start with {MACHINE_MANIFEST_TAG!r}")

    if "machine:" not in text:
        errors.append(f"{manifest_path}: must include machine:")

    web_blocks = re.findall(r"^\s+-\s+id:\s+(\S+)", text, re.MULTILINE)
    seen: set[str] = set()
    for wid in web_blocks:
        if wid in seen:
            errors.append(f"{manifest_path}: duplicate web id {wid!r}")
        seen.add(wid)

    for line_no, line in enumerate(text.splitlines(), start=1):
        if "url:" in line and not re.search(r"url:\s+https?://", line):
            errors.append(f"{manifest_path}:{line_no}: web url must be http(s)")

    return errors


def validate_repo(root: Path) -> list[str]:
    errors: list[str] = []

    machines = machine_dirs(root)
    if not machines:
        errors.append("no machine folders found at repo root")

    for machine in machines:
        manifest = machine / "manifest.yaml"
        errors.extend(validate_manifest(manifest))

        for pdf in sorted(machine.glob("*.pdf")):
            errors.extend(validate_manual_md(pdf.with_suffix(".md"), pdf.name))

        web_dir = machine / "web"
        if web_dir.is_dir():
            for web_md in sorted(web_dir.glob("*.md")):
                errors.extend(validate_web_md(web_md))

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root (default: parent of tools/)",
    )
    args = parser.parse_args(argv)

    errors = validate_repo(args.root.resolve())
    if errors:
        for err in errors:
            print(f"error: {err}", file=sys.stderr)
        print(f"\n{len(errors)} validation error(s)", file=sys.stderr)
        return 1

    print("ok: all PDFs have valid markdown companions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
