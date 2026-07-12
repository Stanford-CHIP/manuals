# Machine manuals

Reference manuals, datasheets, and links for lab equipment. PDFs get AI-readable markdown conversions; web URLs are registered in each machine's manifest.

**For AI models:** read [AGENTS.md](AGENTS.md) before answering questions from this repo.

## Setup

```bash
conda env create -f environment.yml   # or: conda activate manuals if it already exists
conda activate manuals
```

## Add material

1. Create a folder for the machine (e.g. `vinyl-printer-cutter/`).
2. Add or update `manifest.yaml` (see `vinyl-printer-cutter/manifest.yaml`).

**PDFs** — drop the file in the machine folder, then generate markdown:

```bash
python tools/pdf_to_md.py vinyl-printer-cutter
```

**Links** — add manufacturer pages, product pages, download hubs, etc. under `web:` in `manifest.yaml` (each entry needs `id`, `title`, and `url`). No conversion step; models cite these by id (see AGENTS.md). Optional fields: `kind`, `format`, `notes`, `retrieved`.

**Web snapshots** — for HTML you need to quote reliably, save content under `web/<slug>.md` using `tools/web-source-template.md`.

**Lab notes** — for conversation/lab conclusions with a follow-up contact, add `notes/<slug>.md` using `tools/lab-notes-template.md`. Freeze supporting pages under `web/`, list them in the note’s `sources:`, and register live URLs in `manifest.yaml`.

3. Commit PDFs, generated `.md` files, manifest changes, `web/` snapshots, and `notes/` together.

## Validate locally

```bash
python tools/validate.py
```

CI runs the same checks on every PR. The validator enforces:

- At least one machine folder exists at the repo root
- Every `*.pdf` has a sibling `*.md` generated from it
- Each manual `.md` starts with `# format=manual-md`, names its `source_pdf`, and has `## Page N` headings
- If present, `manifest.yaml` uses `# format=machine-manifest`, includes `machine:`, has unique `web` ids, and uses `http(s)` URLs
- Each `web/*.md` snapshot starts with `# format=web-source-md` and includes `source_url:` in its header
- Each `notes/*.md` file starts with `# format=lab-notes-md`, includes `with:`, `date:`, and `sources:`, has Synopsis / Conclusions / Sources headings, and every `sources:` path exists

See [AGENTS.md](AGENTS.md) for how models cite PDFs, manifest links, web snapshots, and lab notes.
