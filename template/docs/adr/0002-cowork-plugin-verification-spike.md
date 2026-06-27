# 2. Cowork plugin verification spike

Date: 2026-01-01

## Status

Accepted (fail-open mandate). Cowork full-enforcement re-test **parked** — blocked on
Anthropic-side Cowork plugin sync, not on us (see Update 2026-06-27).

## Spike result (2026-06-27)

Ran the GUI checklist in a generated project (see
`docs/cowork-verification-checklist.md`):

- **Assumption 1 (hooks fire in Cowork): CONFIRMED.** Plugin PreToolUse hooks
  executed — writes were intercepted, so hooks are not silently skipped.
- **Assumption 2 (`${CLAUDE_PLUGIN_ROOT}` resolves): REFUTED for shell
  expansion.** Cowork did not shell-expand `${CLAUDE_PLUGIN_ROOT}`; the literal
  string reached python, the hook script was not found, python exited 2, and
  Cowork treated exit-2 as a hard block. The guard therefore failed-CLOSED,
  directly violating the fail-open mandate below.
- **Fix applied (`psotobverse-utils` `hooks/hooks.json`):** stop relying on the
  shell to expand `${...}`. Each hook command is now a `python -c` bootstrapper
  that reads `CLAUDE_PLUGIN_ROOT` BY NAME from `os.environ` and `runpy`s the real
  hook; if the env var is absent or the script is missing it exits 0 (FAIL-OPEN).
  Verified locally: enforces when the var is set, fails open when unset.
- **Remaining open question:** does Cowork expose `CLAUDE_PLUGIN_ROOT` as a
  process env var (even though it does not shell-expand it)? If yes, enforcement
  now works in Cowork; if no, the guard degrades to fail-open (safe, no
  enforcement). Re-run the checklist in Cowork to decide, then supersede this ADR.

## Update (2026-06-27) — re-test parked, blocked on Anthropic

We could not get v1.3.1 into Cowork to run the re-test, for reasons external to
this project:

- **Cowork uses a server-side marketplace sync, separate from the Claude Code
  CLI** (`~/.claude`). It compares the repo's latest commit to its last-synced
  commit and skips if unchanged. After pushing v1.3.1 and re-adding the
  marketplace via the CLI, Cowork still served **1.3.0**: its server had not
  re-scanned the repo, and a full Desktop restart did not force a re-scan (it did
  not even rebuild its per-space plugin cache).
- **Third-party/personal marketplaces do not auto-update in Cowork** (only the
  official Anthropic marketplace does), and Cowork's Personal tab has known open
  limitations: cannot add custom marketplaces by URL (anthropics/claude-code
  #66184), personal-marketplace installs lost on restart (#40600).
- Net: getting a custom plugin update into Cowork is currently gated on
  Anthropic's server re-scan cadence / the Cowork plugin preview maturing — not
  on anything in this repo or the companion plugin.

**Decision:** park Cowork enforcement validation. The fix is **shipped and
verified in terminal Claude Code** (where `${CLAUDE_PLUGIN_ROOT}` resolves and
hooks enforce). In Cowork, the guard is now fail-open (safe) rather than
fail-closed. Treat Claude Code as the runtime of record for governed work; revisit
Cowork enforcement when its plugin sync is GA. (A local cache patch can force the
fix into Cowork for an ad-hoc test, but it is not a durable mechanism.)

## Context

This project's governance leans on a **plugin-primary** model: the companion
plugin `psotobverse-utils` (separate repo,
<https://github.com/psotob91/psotobverse-utils>) is meant to carry the shared
hooks, skills, and subagents so the template stays thin and does not duplicate
them. That model rests on two assumptions that we have **not** verified in the
Cowork runtime:

1. **Plugin hooks fire in Cowork.** We assume hooks declared by an installed
   plugin actually trigger during a Cowork session (not only in local Claude
   Code). This is unconfirmed.
2. **`$CLAUDE_PROJECT_DIR` resolves correctly in the Cowork VM.** We assume the
   variable points at the project's working directory inside the Cowork virtual
   machine, so hook scripts can locate repo files. This is unconfirmed.

If either assumption is false, any hard dependency on plugin-enforced
invariants would silently break inside Cowork — the most damaging failure mode
being a "guard" that the user believes is protecting them but never runs.

## Decision

Until both assumptions are verified:

1. **Treat plugin enforcement as fail-open in Cowork.** The `nothing_loose`
   guard (and any other plugin hook relied upon for safety) MUST be designed
   **FAIL-OPEN**: if the hook does not fire or cannot resolve the project
   directory, work proceeds rather than blocking. We do not let an unverified
   mechanism become a silent gate.
2. **Verify via a GUI checklist before trusting the mechanism.** Before
   promoting any plugin hook to a trusted/required control, run a manual
   verification spike in the Cowork GUI:
   - Confirm a trivial plugin hook actually executes during a Cowork session.
   - Confirm `$CLAUDE_PROJECT_DIR` resolves to the expected path in the Cowork VM.
   - Record the outcome in `learning/LEARNING_LOG.md` and supersede this ADR
     with an Accepted decision once confirmed.

## Consequences

- Safety controls behave predictably in Cowork: absent the plugin, nothing
  silently blocks the user, and nothing is falsely assumed to be protecting them.
- There is a known gap: until the spike is done, plugin hooks are
  advisory-only in Cowork and the template must not encode hard dependencies
  on them.
- This ADR is itself a tracked open question; closing it requires a follow-up
  ADR (Accepted or Deprecated) referencing the spike's results.
