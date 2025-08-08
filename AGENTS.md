# Repository Guidelines

## Project Structure & Module Organization
- Source lives in `src/` (or `apps/<name>/src/` for multi-app setups).
- Tests live in `tests/` mirroring package structure (e.g., `tests/foo/test_bar.py` or `src/foo/__tests__/bar.spec.ts`).
- Reusable scripts go in `scripts/`; static assets in `assets/`; docs in `docs/`.

## Coding Style & Naming Conventions
- Formatting: Enforce via toolchain defaults (e.g., Prettier, Black, gofmt, rustfmt). Do not hand-format.
- Indentation: 2 spaces for JS/TS; 4 spaces for Python; language defaults elsewhere.
- Naming: `snake_case` for Python modules/functions, `camelCase` for JS/TS functions/vars, `PascalCase` for types/classes, `kebab-case` for CLI files.
- Keep functions small; prefer pure utilities and clear interfaces.

## Testing Guidelines
- Place unit tests under `tests/` or framework defaults (`__tests__/`).
- Name tests consistently: `test_*.py`, `*.spec.ts`, or `*_test.go`.

## Commit & Pull Request Guidelines
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- Keep commits focused and atomic; include rationale in the body if not obvious.
- PRs: Provide a clear description, link issues (`Closes #123`), include screenshots/logs for UX or CLI changes, and note migration steps if any.
- CI must pass; add/adjust tests when changing behavior.

## Security & Configuration Tips
- Never commit secrets. Store local config in `.env.local`; provide a sanitized `.env.example`.
- Respect `.gitignore`; review diffs for accidental credentials or large binaries.
- Prefer parameterized configs over hard-coded paths and ports.
