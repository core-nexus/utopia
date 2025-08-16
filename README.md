# 🌍 Utopia Node: Building the Future One Node at a Time

Welcome to the first **Utopia Node**—our experiment in AI/human collaboration that cuts through the noise to create real impact.

This isn’t another theoretical framework. It’s a working prototype for knowledge creation that scales without losing its essence.

-----

## What We’re Building

A **Utopia Node** is our solution to the core question: “How do we create knowledge networks that serve consciousness, that uplift all the life?”

Each node is a complete, forkable system designed for autonomous AI purpose work and human flourishing. 

**Content That Ships**  
Deep research, actionable insights, and visual storytelling -- all generated locally with [LM Studio](https://lmstudio.ai). No vendor dependencies, no subscriptions. Pure creative power running on your hardware.

**Foundations That Ground Vision**  
We integrate rigorous science with timeless wisdom and systems thinking. These aren’t philosophical abstractions -- they’re practical lenses that reveal patterns and connections others miss.

**Trust That Scales**  
A decentralized validation layer where quality ideas rise through community consensus. No engagement-optimized algorithms. Just knowledge that genuinely serves humanity.

-----

## The Fractal Vision

Picture thousands of these nodes -- each one a focused laboratory where builders tackle specific aspects of our collective challenges. Fork what resonates, build on what works, let natural selection handle the rest.

This project emerges from [CoreNexus](https://corenexus.is), where human collaboration happens at the interface level. But the real power lies in the underlying architecture -- structures designed for direct collaboration, with or without intermediary layers.

We’re not building another platform. We’re building infrastructure for collective intelligence where:

- Technical precision meets spiritual depth
- Individual insights compose into larger solutions
- Anyone can contribute their unique perspective to the whole

The goal isn’t to create dependency on CoreNexus -- it’s to create systems robust enough to function independently while powerful enough to integrate seamlessly when connected.

**Ready to build something that matters? Clone this repo and start weaving your thread into the larger tapestry.**

-----

*Part of the CoreNexus ecosystem • Designed for autonomous operation • Built for human flourishing*

# Tech Details

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
Prereqs (optional for local rendering): `pandoc`, `marp-cli` (Node).

- Render report to HTML: `bin/docs-html`
- Render report to PDF: `bin/docs-pdf`
- Render slides to HTML: `bin/slides-html`
- Render slides to PDF: `bin/slides-pdf`
- Validate storyboard (optional): `bin/validate-storyboard`
- Clean outputs: `bin/clean`

### Generate a deep-research report
Uses harlantwood/deep-research-cli (branch `cli`). Clones to `./tmp`, pipes `problem.md` to stdin, and writes under `problems/<slug>/solution/report.md`.

- Run: `bin/generate-report` (or `bin/generate-report --problem path/to/problem.md`)
- Output: `problems/<slug>/solution/report.md` with a copy of the input at `problems/<slug>/problem.md`

### Generate a research draft locally
Requires Python and the open_deep_research package on your machine.

1) Install dependencies locally (example):
   - `pip install -U open-deep-research` (or `pip install -U open_deep_research`)
   - Set your provider keys (e.g., `export OPENAI_API_KEY=...` or `ANTHROPIC_API_KEY=...`)

2) Generate a draft from `problem.md`:
   - `bin/generate`
   - Output: `docs/report.draft.md`

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
