# CoreNexus MVP-0

A minimal, Git-native workspace for AI-first collaboration on SDG-aligned gigs. Produces:
- `docs/report.md` → HTML/PDF via Pandoc
- `slides/talk.md` → HTML/PDF via Marp
- `video/storyboard.json` + `video/script.md` → optional stub MP4 (later)

## Structure
- `problem.md` — the task seed
- `docs/` — long-form Markdown with YAML front matter
- `slides/` — Marp-flavoured Markdown for decks
- `video/` — `storyboard.json` (array of scenes) + `script.md`
- `schemas/` — machine-validated JSON Schemas
- `scripts/` — render helpers (local dev)

## Quickstart (local)
Prereqs (optional for local rendering): `pandoc`, `marp-cli` (Node), `make`.

- Render report to HTML: `make docs-html`
- Render report to PDF (needs Pandoc + LaTeX): `make docs-pdf`
- Render slides to HTML: `make slides-html`
- Render slides to PDF: `make slides-pdf`

If tools aren’t installed locally, CI will render on push.

## CI
GitHub Actions workflow in `.github/workflows/build.yml` builds artefacts and uploads them.

## Formats (internal → final)
- Reports: Markdown + YAML front matter → HTML/PDF (Pandoc)
- Slides: Marp Markdown → HTML/PDF (Marp CLI)
- Video: `storyboard.json` + `script.md` → MP4 (future; stub pipeline)

See `schemas/storyboard.schema.json` for storyboard validation.

## Licence / Attribution
Include SPDX and licence in front matter. Default is `CC-BY-4.0` unless changed.
