# Factory watchlist — open items (living, pruned)

A **living** list the maintainer/agent keeps: things to verify, anomalies, and
TODOs so nothing is forgotten. **Prune on resolution** — git history is the
archive; this file is the *open* set. Distinct from `LEARNING_LOG.md`
(append-only) and `PLAYBOOK.md` (durable lessons).

## To verify
- [ ] Confirm the factory hooks fire correctly in a REAL Claude Code session
      (they pass the simulated-stdin test; confirm `SessionStart` additionalContext
      actually appears and `SessionEnd` writes a handoff on a real exit).

## Anomalies / red flags
- [ ] `nothing_loose` write-guard fails open at the factory root (no
      `.claude/policy/paths.allow.json`). Acceptable for now; revisit (see REFLECTOR).

## Later / don't forget
- [ ] Add a root `llms.txt` for the factory (only `template/llms.txt`, the child
      index, exists today — the factory is un-navigable for agents).
- [ ] Decide whether the template's meta-learner hooks should ship from the
      plugin instead of being copied into every child.

<!-- Remove an item when resolved. Keep this list short and current. -->
