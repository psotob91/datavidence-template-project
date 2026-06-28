# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). The
> `SessionStart` hook injects its head so a new session resumes cheaply (in the
> **terminal**; in the **desktop app** read this file yourself — see below).
> Durable history lives in `learning/sessions/` (handoffs) and `git log`.

- **Updated:** 2026-06-28
- **Branch (git local):** `main` — everything integrated **and pushed** to `origin/main`.
- **Status:** Desktop-hooks fix shipped (plugin **v1.6.0**) + stale-render-tag fix shipped. All clean & pushed. **Restart the desktop app if it isn't already on v1.6.0.**

## Done (this milestone)
- **Meta-learner now works in the desktop app.** Root cause: desktop fires plugin hooks but does NOT set `CLAUDE_PLUGIN_ROOT` (old bootstrapper fired-but-no-op'd). Fix = self-discovering bootstrapper in `psotobverse-utils` **v1.6.0** (pushed + `marketplace/plugin update` done; verified). Layer-2 limit (desktop doesn't inject `SessionStart` stdout, Anthropic #47993) worked around by a "read `SESSION_STATE.md` yourself" directive in `CLAUDE.md` + `template/CLAUDE.md.jinja` — **verified live**: a fresh desktop session read it on its own. Side-effecting hooks (signals, handoff, dirty-bit) run in desktop. See [[desktop-hooks-clauderoot]].
- **Fixed the stale render tag.** `new-study.ps1` + `template-ci.yml` now pass `--vcs-ref=HEAD` (CI also `fetch-depth: 0`) — Copier was defaulting to the old `v0.1.0` tag. All 4 profiles render from HEAD and pass `check_placeholders`.
- Factory `main` pushed to GitHub (the whole R-rigor + meta-learner body + these fixes).

## Next steps (pending)
1. Resolve `temporal-expansion-ideas/` (untracked, superseded): prose-ify into `docs/research/` or archive + `.gitignore`; finish `routinely-collected-data.md` stub.
2. Fix the `datavidence-healthanalysis` plugin reference (routed to but not installed): ship / repoint / mark planned.
3. Root `llms.txt` for the factory; extend CI to render-and-validate (beyond check_placeholders).
4. Optional: factory `.claude/policy/paths.allow.json` to activate the `nothing_loose` write-guard.
5. Optional: start tagging releases (e.g. `v0.2.0`) so plain `copier copy` / `copier update` track releases (the `--vcs-ref=HEAD` fix covers our own script + CI for now).

## Uncommitted
- `temporal-expansion-ideas/` (untracked roadmap — see step 1). Everything else committed + pushed.

## Machine note
- Env cache (`~/.claude/environment.md`) on this PC reports `make` and `rg` **present** (earlier "missing make+rg" notes are stale).
