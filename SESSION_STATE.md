# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). The
> `SessionStart` hook injects its head so a new session resumes cheaply. Durable
> history lives in `learning/sessions/` (handoffs) and `git log`; this file is
> only "where we are right now + what's next".

- **Updated:** 2026-06-28
- **Branch:** `feat/r-rigor-expansion`
- **Status:** meta-learner refactored to the plugin (v1.4.0) + factory/template slimmed to opt-in config; all render- and lifecycle-tested. **Uncommitted in 2 repos, pending user OK to commit + push.**

## Done this session
- Advanced 11-agent audit (13/13 claims confirmed) → `docs/audits/2026-06-28-repo-audit/`.
- Built the meta-learner, then **refactored the generic mechanism INTO the plugin** `psotobverse-utils` **v1.4.0** (session hooks + `/reflect` + `/audit-report`), OPT-IN per project via `.claude/meta-learner.json`. Tested: no-op without config, active with config, crash-detect, handoff, render.
- Factory + template now carry only **config + data + routing** (`.claude/meta-learner.json`, `learning/*`, radars, `SESSION_STATE`, constitution rule 9, CLAUDE.md routing). Duplicated hook scripts removed.
- Closed parity gaps: factory CLAUDE.md plugin-routing; `template/SESSION_STATE.md.jinja` seed.

## Next steps (in priority order)
1. **Plugin release:** push `C:/workspace/psotobverse-utils` (v1.4.0) to GitHub, then `/plugin marketplace update psotobverse-utils` + `/plugin update psotobverse-utils`. Until then the session hooks/skills are absent (repos still work). **Needs user OK (push is outward-facing).**
2. Commit the datavidence changes (this repo) — branch `feat/r-rigor-expansion` or a new `feat/meta-learner`.
3. Resolve `temporal-expansion-ideas/` (untracked, superseded): prose-ify briefs into `docs/research/` or archive + gitignore; finish `routinely-collected-data.md` stub.
4. Fix the `datavidence-healthanalysis` plugin reference (not installed): ship / repoint / mark planned.
5. Root `llms.txt` for the factory; CI render-and-validate; optional factory `paths.allow.json`.

## Uncommitted
- **datavidence** (this repo): `.claude/meta-learner.json`, `CLAUDE.md`, `SESSION_STATE.md`, `learning/`, `docs/audits/`, `.gitignore`, `CHANGELOG`; `template/.claude/{meta-learner.json,constitution.md}`, `template/CLAUDE.md.jinja`, `template/learning/CONSENSUS_WATCH.md`, `template/SESSION_STATE.md.jinja`, `template/.gitignore`, `template/learning/REFLECTOR.md`, `template/docs/audits/`; pre-existing `template/docs/analysis/modules/causal.md`.
- **psotobverse-utils** (`C:/workspace/psotobverse-utils`): `hooks/{meta_util,session_start,capture_signal,session_end}.py`, `hooks/hooks.json`, `skills/{reflect,audit-report}/SKILL.md`, `plugin.json` (v1.4.0), `CHANGELOG.md`.
