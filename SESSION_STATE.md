# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). The
> `SessionStart` hook injects its head so a new session resumes cheaply. Durable
> history lives in `learning/sessions/` (handoffs) and `git log`; this file is
> only "where we are right now + what's next".

- **Updated:** 2026-06-28
- **Branch (git local):** `main` — everything integrated here.
- **Status:** R-rigor expansion + meta-learner fully merged to `main`; plugin v1.4.0 live. Done & tested.

## Done (this milestone)
- Merged the git branch `feat/r-rigor-expansion` (stages 1–5: R analysis governance) into `main` — no conflicts.
- Completed the meta-learner wiring on `main` (constitution rule 9, CLAUDE.md.jinja Meta-learner section, REFLECTOR consensus lane) — the earlier partial commit's stashed edits.
- Tested: Copier renders **A** (R/standard) and **B** (R/health-data/all modules) both PASS `check_placeholders`; meta-learner + R-rigor coexist; gating correct.
- `psotobverse-utils` **v1.4.0**: pushed to GitHub remote, marketplace refreshed, installed pointer flipped to 1.4.0 (verified via `claude plugin list/details`). **Restart Claude for the session hooks to load in this repo.**

## Next steps (pending, lower priority)
1. Resolve `temporal-expansion-ideas/` (untracked, superseded): prose-ify the two Gemini briefs into `docs/research/` or archive + `.gitignore`; finish `routinely-collected-data.md` stub.
2. Fix the `datavidence-healthanalysis` plugin reference (routed to from `data-onboarding.md` + modules but not installed): ship / repoint / mark planned.
3. Root `llms.txt` for the factory; extend CI to render-and-validate (not just check_placeholders).
4. Optional: factory `.claude/policy/paths.allow.json` to activate the `nothing_loose` write-guard.
5. Push `main` (datavidence) to its GitHub remote when ready.

## Uncommitted
- `temporal-expansion-ideas/` (untracked roadmap — see step 1).
- Backup left at `~/.claude/plugins/installed_plugins.json.bak` (safe to delete).
