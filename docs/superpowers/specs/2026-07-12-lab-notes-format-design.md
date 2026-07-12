# Lab notes format design

date: 2026-07-12
status: approved for implementation

## Goal

Capture lab / conversation conclusions about machine supplies (starting with printable HTV) as first-class citable repo content, with frozen web sources and a named follow-up contact.

## Format

- Path: `<machine>/notes/<slug>.md`
- Tag: `# format=lab-notes-md`
- Required header fields: `title`, `machine`, `with`, `date`, `sources` (list of paths relative to the machine folder)
- Required body headings: `## Synopsis`, `## Conclusions`, `## Sources`

## Rules

- Product facts in conclusions must be backed by frozen `web/*.md`, in-repo PDF markdown, or both
- `with:` names who to talk to if a model picks up the thread
- Manifest `web:` entries register live URLs; `web/*.md` holds frozen copies

## Validation

`tools/validate.py` checks notes headers, required headings, and that every `sources:` path exists.
