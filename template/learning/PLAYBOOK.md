# Playbook

**Distilled, read before a task.** This is the curated, high-signal companion
to `LEARNING_LOG.md`: only conclusions that have proven reusable belong here.
Keep it short — if it stops being true, fix it (and log the correction).

## Environment

- Analysis stack is R by default: `renv` for dependencies, `{targets}` for the
  pipeline, Quarto for reporting. The tooling/harness layer is Python stdlib.
- Lockfiles (`renv.lock` / `uv.lock`) are NOT committed; regenerate with
  `make setup` on a fresh checkout.
- Run the pipeline with `make pipeline` (`targets::tar_make()`); tests with
  `make test`; full check with `make check`.

## Patterns that work

- Put reusable functions in `R/`, keep `_targets.R` as orchestration only.
- One self-contained deliverable per task under `outputs/<slug>/` (see
  `outputs/OUTPUT_LAYOUT.md`).
- Record significant decisions as ADRs under `docs/adr/` before implementing.

## Gotchas

- Do NOT run `/init`; a curated `CLAUDE.md` already exists and `/init` would
  clobber the governance setup.
- In Cowork, plugin hooks are unverified and fail-open — do not rely on them as
  hard guards (see `docs/adr/0002-cowork-plugin-verification-spike.md`).
- `llms.txt` is generated; edit the source files and run `make reindex`.

## Optimal disclosure

- Read in this order: `.claude/constitution.md` → `.claude/policies/00-index.md`
  → `.claude/knowledge-map.md` → `PROJECT_BRIEF.md`.
- Pull detail on demand from the knowledge map; do not preload everything.
