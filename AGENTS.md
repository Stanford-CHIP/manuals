# Manuals repository — instructions for AI models

This repository stores machine manuals, datasheets, and related reference material. Use it as the **primary source** when answering questions about equipment documented here.

## Core rules

1. **Answer from sources only.** Do not invent specifications, procedures, warnings, or part numbers that do not appear in a file in this repo.
2. **Cite every factual claim.** Each statement taken from a source must include a citation (see formats below).
3. **Use exact page numbers for PDF-derived content.** Page numbers come from the `## Page N` headings in `*.md` files converted from PDFs. Quote or paraphrase only what appears on the cited page(s).
4. **Say when information is missing.** If the manuals do not cover a question, say so explicitly. Do not guess or fill gaps from general knowledge unless the user asks for general background *and* you clearly label it as outside this repo.
5. **Prefer markdown over PDF.** Read the sibling `*.md` file for each PDF. Open the PDF only when the markdown is unclear or you need to verify layout, diagrams, or tables.

## Repository layout

```
<machine-slug>/
  manifest.yaml       # machine metadata + web link registry
  <name>.pdf          # original document (source of truth for PDF content)
  <name>.md           # AI-readable conversion (required for every PDF)
  web/                # optional: saved web content as citable markdown
    <slug>.md
  notes/              # optional: lab / conversation notes (lab-notes-md)
    <slug>.md
```

Machine folders are top-level directories (e.g. `vinyl-printer-cutter/`). Ignore `tools/`, `docs/`, and `.github/`.

## Citation formats

### PDF-derived manuals (`# format=manual-md`)

```text
[vinyl-printer-cutter/BN2-20_INS2_EN.md, Page 12]
```

Or inline: *"Load media from the rear tray"* (BN2-20_INS2_EN.md, Page 12).

Use the page number from the nearest preceding `## Page N` heading. If content spans pages, cite all relevant pages.

### Web links (from `manifest.yaml`)

For URLs listed under `web:` in a machine's manifest — cite the link when you used it, but treat it as **external**: content may change and is not guaranteed to match a frozen page in this repo.

```text
[vinyl-printer-cutter/manifest.yaml → roland-bn20-product]
```

Include the `url` from the manifest entry in your answer when helpful.

### Saved web pages (`# format=web-source-md`)

Files under `<machine>/web/*.md` are frozen snapshots. Cite by file path and section heading:

```text
[vinyl-printer-cutter/web/driver-install.md → ## Windows installation]
```

If the file has a `retrieved:` date in its header, mention it when the currency of the information matters.

### Lab notes (`# format=lab-notes-md`)

Files under `<machine>/notes/*.md` capture lab or conversation conclusions. Header must include `with:` (who to follow up with), `date:`, and `sources:` listing frozen `web/*.md` and/or in-repo manual paths. Cite synopsis/conclusions from the note; cite product facts from the frozen sources or PDFs the note points to:

```text
[vinyl-printer-cutter/notes/printable-htv-clear-vs-opaque.md → ## Conclusions]
[vinyl-printer-cutter/web/stahls-supertek-matte-clear.md → ## Key constraints]
```

Do not treat unsourced statements in a note as stronger than the frozen pages they cite.

## How to answer a question

1. Identify which machine folder(s) apply.
2. Read `manifest.yaml` for context and registered web links.
3. Search/read relevant `*.md` files (PDF conversions, `web/*.md`, and `notes/*.md`).
4. Compose an answer using only verified content; attach citations per claim.
5. If sources conflict, note the conflict and cite both.

## Regenerating markdown from PDF

Contributors run:

```bash
pip install -r requirements.txt
python tools/pdf_to_md.py <machine-folder>
```

CI enforces that every `*.pdf` has a matching `*.md`. Do not hand-edit page headings in converted files — regenerate from the PDF instead.
