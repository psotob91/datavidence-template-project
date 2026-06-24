# Reflector

**Triage candidate improvements.** Raw ideas, frictions, and "we should
maybe..." land here first. Each gets sorted into one of four lanes. Promote
durable conclusions into `PLAYBOOK.md`; record what actually happened in
`LEARNING_LOG.md`.

Review this board at the end of a work session.

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
