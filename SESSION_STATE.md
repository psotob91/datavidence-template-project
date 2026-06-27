# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). The
> `SessionStart` hook injects its head so a new session resumes cheaply. Durable
> history lives in `learning/sessions/` (handoffs) and `git log`; this file is
> only "where we are right now + what's next".

- **Updated:** 2026-06-28
- **Branch (git local):** `main` — everything integrated here.
- **Status:** R-rigor + meta-learner merged to `main`; plugin **v1.5.0** live (adds once-per-machine environment probe). Done & tested. **Restart Claude to load the new session hooks.**

## Done (this milestone)
- Merged the git branch `feat/r-rigor-expansion` (stages 1–5: R analysis governance) into `main` — no conflicts; completed the meta-learner wiring (constitution rule 9, CLAUDE.md.jinja section, REFLECTOR lane).
- Tested: Copier renders **A** (R/standard) and **B** (R/health-data/all modules) both PASS `check_placeholders`.
- `psotobverse-utils` → **v1.4.0** (meta-learner) → **v1.5.0** (environment probe in SessionStart). Pushed to GitHub; updated via the correct flow (`marketplace update` → `claude plugin update <plugin>@<marketplace>`). Env cache at `~/.claude/environment.json` (this PC: Win10/PS5.1, missing `make`+`rg`).
- Learned + memorized: the plugin-update procedure (was using `install`, idempotent) and the environment-probe system.

## Next steps (pending, lower priority)
1. Resolve `temporal-expansion-ideas/` (untracked, superseded): prose-ify the two Gemini briefs into `docs/research/` or archive + `.gitignore`; finish `routinely-collected-data.md` stub.
2. Fix the `datavidence-healthanalysis` plugin reference (routed to from `data-onboarding.md` + modules but not installed): ship / repoint / mark planned.
3. Root `llms.txt` for the factory; extend CI to render-and-validate (not just check_placeholders).
4. Optional: factory `.claude/policy/paths.allow.json` to activate the `nothing_loose` write-guard.
5. Push `main` (datavidence) to its GitHub remote when ready.

## Uncommitted
- `temporal-expansion-ideas/` (untracked roadmap — see step 1).
- Backup left at `~/.claude/plugins/installed_plugins.json.bak` (safe to delete).
