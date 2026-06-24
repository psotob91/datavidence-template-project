# Anti-drift

Keep work anchored to the charter and recorded decisions over a long session.

## Rules

- **Do not derive from the constitution or recorded decisions.** If a step
  would contradict `constitution.md` or an entry in `docs/adr/`, it is wrong —
  the step changes, not the rule.
- **Respect the document hierarchy.** Authority flows: constitution > policies >
  recorded decisions (`docs/adr/`) > project brief > working notes. Lower
  artifacts must not silently override higher ones.
- **Stop and name the principle at risk.** When you feel pressure to cut a
  corner, pause and state plainly which rule or decision is about to be violated,
  then choose deliberately rather than drifting into it.
- **Size hygiene (soft token budget per artifact).** Keep each artifact within a
  soft budget: `CLAUDE.md` and the charter stay lean, policies stay atomic,
  notes stay short. When an artifact bloats, split or prune it before adding more.
- **Label epistemic status.** Tag content as fact, decision, or hypothesis so
  later steps do not mistake a guess for settled ground.

## Check

If a later step contradicts an earlier decision, the drift is the bug. Reconcile
against the higher artifact; do not quietly let the newer text win.
