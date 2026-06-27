# Factory Reflector

**Triage candidate improvements** for the factory. Raw ideas, frictions, and "we
should maybe…" land here first (the `/reflect` skill proposes additions from the
signal queue), then get sorted into one of four lanes. Promote durable
conclusions into `PLAYBOOK.md`; record what happened in `LEARNING_LOG.md`; track
emerging Anthropic conventions in `STANDARDS_WATCH.md`.

Review this board at the end of a work session (or when `/reflect` runs).

## Now — act on this session

- Fix the `datavidence-healthanalysis` plugin reference: it is routed to from
  `template/.claude/policies/analysis/data-onboarding.md` and module docs but is
  not installed — children are told to call skills that do not exist.
- Resolve `temporal-expansion-ideas/`: prose-ify the two Gemini briefs into
  `docs/research/` (or archive under `docs/research/archive/` + gitignore) and
  remove the dangling forward-reference from the `routinely-collected-data.md` stub.

## Defer — revisit when a trigger fires

Each item MUST name an explicit **TRIGGER**.

- Add a factory `.claude/policy/paths.allow.json` to activate the `nothing_loose`
  write-guard — **TRIGGER:** when loose files start landing in the factory root.

## Optional — nice to have, no urgency

- A root `llms.txt` validation in CI (links resolve, structure matches llmstxt.org).

## Discard — decided against

- (none yet) — _each discarded item MUST state **no re-propose** + a one-line reason._
