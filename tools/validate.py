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
LAB_NOTES_MD_TAG = "# format=lab-notes-md"
MACHINE_MANIFEST_TAG = "# format=machine-manifest"

LAB_NOTES_REQUIRED_HEADINGS = ("## Synopsis", "## Conclusions", "## Sources")
LAB_NOTES_REQUIRED_FIELDS = ("title:", "machine:", "with:", "date:", "sources:")


def machine_dirs(root: Path) -> list[Path]:
    skip = {"tools", ".github", ".git", ".cursor", "docs"}
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


def _header_block(text: str) -> str:
    if "\n---\n" in text:
        return text.split("\n---\n", 1)[0]
    return text.split("---", 1)[0]


def _parse_sources(header: str) -> list[str]:
    """Parse YAML-ish sources: list under a sources: key."""
    lines = header.splitlines()
    sources: list[str] = []
    in_sources = False
    for line in lines:
        if re.match(r"^sources:\s*$", line):
            in_sources = True
            continue
        if in_sources:
            m = re.match(r"^\s+-\s+(\S+)\s*$", line)
            if m:
                sources.append(m.group(1))
                continue
            if re.match(r"^[a-zA-Z_][\w-]*:", line):
                break
            if line.strip() == "":
                continue
            break
    return sources


def validate_lab_notes_md(md_path: Path, machine_dir: Path) -> list[str]:
    errors: list[str] = []
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith(LAB_NOTES_MD_TAG):
        errors.append(f"{md_path}: must start with {LAB_NOTES_MD_TAG!r}")
        return errors

    header = _header_block(text)
    for field in LAB_NOTES_REQUIRED_FIELDS:
        if field not in header:
            errors.append(f"{md_path}: header must include {field}")

    for heading in LAB_NOTES_REQUIRED_HEADINGS:
        if not re.search(rf"^{re.escape(heading)}$", text, re.MULTILINE):
            errors.append(f"{md_path}: missing required heading {heading!r}")

    sources = _parse_sources(header)
    if not sources:
        errors.append(f"{md_path}: sources: must list at least one path")
    for rel in sources:
        target = machine_dir / rel
        if not target.is_file():
            errors.append(f"{md_path}: sources entry not found: {rel}")

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

        notes_dir = machine / "notes"
        if notes_dir.is_dir():
            for notes_md in sorted(notes_dir.glob("*.md")):
                errors.extend(validate_lab_notes_md(notes_md, machine))

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
