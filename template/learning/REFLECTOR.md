# Reflector

**Triage candidate improvements.** Raw ideas, frictions, and "we should
maybe..." land here first. Each gets sorted into one of the lanes below. Promote
durable conclusions into `PLAYBOOK.md`; record what actually happened in
`LEARNING_LOG.md`; route methodological standards/controversies to
`CONSENSUS_WATCH.md`.

Review this board at the end of a work session (the `/reflect` skill proposes
additions from the captured signal queue — it never auto-edits).

## Consensus & method signals — escalate, don't decide

Methodological observations the agent flagged: a possible new/shifting consensus,
a controversy, or a suspected bad practice (e.g. Table 2 fallacy, confounder
treated as prognostic factor, adjusting for a mediator/collider, immortal-time
bias). **These are surfaced to the user with a recommended validation, never
acted on unilaterally.** Durable ones graduate to `CONSENSUS_WATCH.md`.

- (none yet) — _example: "User says the guideline we cited for X was superseded —
  TRIGGER: confirm against the primary EQUATOR/GRADE source, then update
  CONSENSUS_WATCH and ask before changing the analysis."_

## Now — act on this session

Improvements worth doing immediately, before moving on.

- (none yet)

## Defer — revisit when a trigger fires

Each deferred item MUST name an explicit **TRIGGER** (the condition that should
bring it back). No trigger → it does not belong here.

- (none yet) — _example: "Add caching to the import target — TRIGGER: when raw
  data exceeds 1 GB and `tar_make()` takes over 5 min."_

## Optional — nice to have, no urgency

Low-priority polish; pick up only with spare capacity.

- (none yet)

## Discard — decided against

Each discarded item MUST state **no re-propose** and a one-line reason, so the
same idea is not relitigated.

- (none yet) — _example: "Commit renv.lock to the template — no re-propose:
  children must regenerate it via `make setup` (see CLAUDE.md / constitution)."_
