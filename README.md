# 🌍 Utopia Node: The First Step to a Fractal Future

Welcome to the first **Utopia Node**, a playground for human 🤝 AI collaboration on a whole new level.  
Here, we’re not just solving problems—we’re weaving a living, evolving tapestry of solutions.  

Think of this as your gateway to a **fractal network of knowledge**, where each node is a microcosm of the whole, and every contribution helps shape a better world. ✨

---

## 🚀 What is a Utopia Node?

A **Utopia Node** is a self-contained, forkable repository designed to tackle pieces of the world’s biggest puzzles through a spectrum of lenses. Each node includes:

- 📑 **Content**: Deep research reports, slides, storyboards, and even AI-generated videos.  
  All created locally using [LM Studio](https://lmstudio.ai) and open models—no cloud fees, just the cost of electricity. ⚡

- 🌀 **Foundations**: A set of philosophical and contextual lenses that integrate science, spirituality, and systems thinking.  
  These help us frame problems holistically and organize knowledge so every node fits into the larger fractal.

- 🔗 **Trust**: A decentralized trust layer where nodes and their content can be validated by the community.  
  This ensures the best ideas rise to the top, creating a web of trusted knowledge.

---

## 🌐 How It All Fits Together

Imagine millions of these nodes, each a **mini-laboratory of innovation**, forking and merging to create a global tapestry of solutions. 🧩  

With the [CoreNexus](https://corenexus.is) interface, you will be able to:

- Navigate this fractal network  
- Discover trusted insights  
- Contribute your own unique perspective  

We’re building a living, breathing ecosystem where everyone—humans *and* AIs alike—can help co-create a better future. 💡

✨ **Join us, fork a node, and start shaping utopia.**

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
