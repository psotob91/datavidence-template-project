# 0002. Generic routing mechanism + recall safety net

Date: 2026-06-28

## Status

Accepted

## Context

The policy set encodes ~30 conditional "knowledge-flow" edges in prose (e.g. clinical
codes → phenotyping; observational-non-routine → causal). Two risks:

1. **Saturation** — wiring every policy to every other (~40 nodes ⇒ ~780 edges) is an
   unmaintainable tangle.
2. **False negatives** — a predicate-gated router that *filters* could silently drop a
   relevant policy that no rule fired on ("a path blocks and we never see a key policy").

We also need the routing *enforced* (hooks), but the domain plugin
(`datavidence-healthanalysis`) is intentionally blueprint-only, and the guardrail plugin
(`psotobverse-utils`) must stay orthogonal (reusable across projects, no health specifics).

## Decision

- **Hub-routed sparse DAG.** One always-reachable hub (policy index + knowledge-map)
  guarantees no dead-ends; each policy has bounded out-degree (≤3: prerequisites + 1–3
  conditional next-steps); every conditional edge carries a **trigger predicate** and is
  bypassed when false. O(n) edges, not O(n²).
- **Invariant 0 — routing is additive, never subtractive.** Predicates only *suggest*
  the next policy; they never hide or forbid *reading* any policy. `block` mode applies
  only to a load-bearing *write* (e.g. phenotype code before its timeline), never to
  consulting a policy.
- **Generic mechanism, child-shipped data.** The routing engine
  (`policy_router`, `comprehension_gate`) and the recall panel (`/coverage`) live in
  `psotobverse-utils` and are driven by data the child ships
  (`template/.claude/policy/routing.yml`). The engine no-ops without that file — the same
  orthogonality the meta-learner uses (`meta-learner.json`). The domain plugin therefore
  needs no new hooks; its gates become `routing.yml` rows.
- **Recall safety net.** `/coverage` fans out N Sonnet agents with *decorrelated lenses*
  (data-type / study-design / output / failure-mode / adversarial-escape), aggregates by
  **union** (recall) and **votes** (triage: Tier-1 ≥majority must-read, Tier-2 ≥1
  consider), with **negative justification** for excluded groups; Opus synthesizes.
  Union miss ≈ pᴺ only when errors are decorrelated, so diversity is the mechanism. The
  claim is **benchmarked**, not asserted (`eval/coverage/`).

## Consequences

- The ~30 edges are surfaced + gated, not multiplied; the index is the single hub.
- The factory and children share one routing engine; health stays out of the engine.
- A measured recall benchmark guards against regressions in coverage.
- Cross-repo work caveat: `nothing_loose` denies writes outside `CLAUDE_PROJECT_DIR`, so
  the factory's own `paths.allow.json` is activated last (see SESSION_STATE / M4b).
