# 2. Cowork plugin verification spike

Date: 2026-01-01

## Status

Proposed

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
