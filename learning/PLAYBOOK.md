# Factory Playbook

**Distilled, read before a task.** Curated, high-signal guidance for maintaining
the **template factory** (this repo), not the analysis work inside a child. Keep
it short; if a line stops being true, fix it and log the correction in
`LEARNING_LOG.md`.

## What this repo is

- This repo is a **Copier factory**, not a project. `copier.yml` sets
  `_subdirectory: template`, so **everything under `template/` is the rendered
  CHILD**; everything at the root governs the **factory itself** and is NOT
  rendered. Master = factory; each generated child = product.
- Never hand-edit generated output. Edit the `.jinja` source under `template/`,
  then re-render. Verify with the render matrix (`.github/workflows/template-ci.yml`).

## Patterns that work

- Two `CLAUDE.md` files, different audiences: the **root `CLAUDE.md`** (this
  layer) is for template MAINTAINERS; **`template/CLAUDE.md.jinja`** governs
  generated children. Do not conflate them.
- Hooks are Python stdlib, no venv, and use the portable bootstrapper
  (`python -c` reading `CLAUDE_PROJECT_DIR` from `os.environ`, fail-open). Test a
  hook by piping simulated stdin JSON to the script before wiring it.
- Keep the meta-learner hybrid: cheap append-only capture during the session
  (`UserPromptSubmit`), a deterministic skeleton on `SessionEnd`, and a
  **human-gated** `/reflect` for synthesis. Never let a hook silently edit a
  learning file.

## Gotchas

- Do NOT run `/init`; this curated `CLAUDE.md` is authoritative and `/init` would
  clobber it.
- The `psotobverse-utils` plugin hooks fire at USER scope (every session). The
  write-guard `nothing_loose` FAILS OPEN here because the factory root has no
  `.claude/policy/paths.allow.json` — add one only if you want write-allowlisting
  at the factory level (it will start checking your writes immediately).
- `template/llms.txt` is the CHILD's index; the factory has its own root
  `llms.txt`. Regenerate the child's with `make reindex` inside a render.

## Optimal disclosure (read order for a new session)

1. Root `CLAUDE.md` → 2. `SESSION_STATE.md` (current state) →
3. `git log --oneline -8` → 4. pull detail on demand from `CHANGELOG.md`,
the relevant ADR, and `learning/sessions/` handoffs. Do not preload `template/`.
