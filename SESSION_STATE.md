# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). The
> `SessionStart` hook injects its head so a new session resumes cheaply (in the
> **terminal**; in the **desktop app** read this file yourself — see below).
> Durable history lives in `learning/sessions/` (handoffs) and `git log`.

- **Updated:** 2026-06-28
- **Branch (git local):** `main` — everything integrated here.
- **Status:** Desktop-hooks fix shipped. Plugin **v1.6.0** live & pushed. **Restart the desktop app to load v1.6.0.**

## Done (this milestone)
- **Diagnosed why the meta-learner didn't inject in the desktop app** (`CLAUDE_CODE_ENTRYPOINT=claude-desktop`). Two layers: (1) desktop fires plugin hooks but does NOT set `CLAUDE_PLUGIN_ROOT`, so the old bootstrapper fired-but-no-op'd; (2) even fixed, the desktop does NOT inject `SessionStart` stdout into the model (Anthropic #47993). Verified empirically (marker-hook probe + `session.json` written + a fresh desktop session reporting no injection).
- **Fixed layer 1:** self-discovering bootstrapper (tries `CLAUDE_PLUGIN_ROOT`, else `installed_plugins.json`→`installPath`, else cache glob; fail-open; terminal unchanged). Shipped to `psotobverse-utils` **v1.6.0**, pushed, `marketplace update`→`plugin update` done (cache now 1.6.0; verified emits 3156 B with the env var unset). Side-effecting hooks (signal capture, handoff, dirty-bit) now run in desktop.
- **Worked around layer 2 (parity):** added a "read `SESSION_STATE.md` yourself at session start in the desktop app" directive to `CLAUDE.md` and `template/CLAUDE.md.jinja`; bumped the plugin floor to ≥ v1.6.0 in both. (`CLAUDE.md` IS injected in desktop; the hook's stdout is not.)
- Memorized the desktop-hooks finding ([[desktop-hooks-clauderoot]]).

## Next steps (pending)
1. **Stale render tag:** `scripts/new-study.ps1` runs `copier copy --defaults` with **no `--vcs-ref=HEAD`**, so new children render the old tag **`v0.1.0`** (pre-meta-learner, pre-desktop guidance). Fix: add `--vcs-ref=HEAD` to the script *or* tag a current release (e.g. `v0.2.0`). Confirm what the CI render matrix uses too.
2. Resolve `temporal-expansion-ideas/` (untracked, superseded): prose-ify into `docs/research/` or archive + `.gitignore`; finish `routinely-collected-data.md` stub.
3. Fix the `datavidence-healthanalysis` plugin reference (routed to but not installed): ship / repoint / mark planned.
4. Root `llms.txt` for the factory; extend CI to render-and-validate (not just check_placeholders).
5. Optional: factory `.claude/policy/paths.allow.json` to activate the `nothing_loose` write-guard.

## Uncommitted
- Factory: `CLAUDE.md` + `template/CLAUDE.md.jinja` (self-read directive) committed this session; **factory `main` not yet pushed** (push when ready).
- `temporal-expansion-ideas/` (untracked roadmap — see step 2).

## Machine note
- Env cache (`~/.claude/environment.md`) on this PC now reports `make` and `rg` **present** (earlier notes saying "missing make+rg" are stale).
