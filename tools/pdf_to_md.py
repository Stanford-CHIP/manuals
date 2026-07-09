#!/usr/bin/env python3
"""Convert PDF manuals to page-structured markdown for AI consumption."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import fitz  # pymupdf

FORMAT_TAG = "# format=manual-md"
REPO_ROOT = Path(__file__).resolve().parent.parent


def slug_from_path(pdf_path: Path, machine_dir: Path) -> str:
    return machine_dir.name


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def pdf_to_markdown(pdf_path: Path, machine_dir: Path) -> str:
    doc = fitz.open(pdf_path)
    machine = slug_from_path(pdf_path, machine_dir)
    title = pdf_path.stem.replace("_", " ")

    parts = [
        FORMAT_TAG,
        "",
        f"title: {title}",
        f"source_pdf: {pdf_path.name}",
        f"machine: {machine}",
        f"pages: {doc.page_count}",
        "",
        "---",
        "",
        f"# {title}",
        "",
    ]

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = clean_text(page.get_text())
        parts.append(f"## Page {page_num + 1}")
        parts.append("")
        parts.append(text if text else "_(no extractable text on this page)_")
        parts.append("")

    doc.close()
    return "\n".join(parts).rstrip() + "\n"


def convert_pdf(pdf_path: Path, *, dry_run: bool = False) -> Path:
    md_path = pdf_path.with_suffix(".md")
    content = pdf_to_markdown(pdf_path, pdf_path.parent)
    if dry_run:
        print(f"would write {md_path} ({len(content)} bytes)")
        return md_path
    md_path.write_text(content, encoding="utf-8")
    print(f"wrote {md_path}")
    return md_path


def discover_pdfs(target: Path) -> list[Path]:
    if target.is_file() and target.suffix.lower() == ".pdf":
        return [target]
    if target.is_dir():
        return sorted(target.rglob("*.pdf"))
    return []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="PDF file(s) or machine folder(s) under the repo root",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without creating files",
    )
    args = parser.parse_args(argv)

    pdfs: list[Path] = []
    for path in args.paths:
        resolved = path if path.is_absolute() else REPO_ROOT / path
        pdfs.extend(discover_pdfs(resolved))

    # skip tooling / dot dirs
    pdfs = [
        p
        for p in pdfs
        if "tools" not in p.parts and not any(part.startswith(".") for part in p.parts)
    ]

    if not pdfs:
        print("no PDF files found", file=sys.stderr)
        return 1

    for pdf in pdfs:
        convert_pdf(pdf, dry_run=args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
