# 0003. Mandatory analysis pre-registration (modular folder + single lock)

Date: 2026-06-28

## Status

Proposed (spec for review — not yet built)

## Context

The tsukuba audit (`docs/audits/2026-06-28-tsukuba-audit/`) found a good pre-registration
*idea* but a **distributed, unenforced** implementation: the SAP was scattered across
`sap.md` + `estimand.yaml` + `objectives.yaml` + a 1,600-line decision matrix, with no
single lockable artifact and nothing blocking analysis before it existed. The owner's
requirement: pre-registering the analysis plan + basic protocol must be **mandatory**,
**harmonized from arbitrary inputs**, **human-readable** (a methods appendix / paper-ready)
but **not contaminated** by agent-only comprehension artifacts, and it must carry the
**selection-criteria → flow-diagram → population-cascade → variable-definition** spine
*from the start*. (Stage 2, deferred: publish to an open registry with deviations.)

## Decision

Ship a **per-objective modular `analysis-plan/`**: a small **shared** layer plus one folder
**per objective**, each objective carrying its **own SAP and its own lock**. The gate is
**per objective** — a locked objective advances even while another is still draft (one never
blocks the other). Filled by the `frame-study` skill, enforced by a `sap-lock` hook. The
folder is **human-canonical** (paper-ready); agent comprehension artifacts live under
`context/`. Renders when `analysis_stack == 'r'` (health-data adds eligibility/phenotype
nuance).

### 1. Folder structure (`template/analysis-plan/`, rendered into the child)

Primary and secondary objectives have **different** analysis plans, and their **selection
criteria may be shared or vary** (both supported). A shared layer holds the study-level
common parts; each objective overrides/extends as needed and owns its lock.

```
analysis-plan/
  shared/                          # study-level, common to all objectives
    study.yaml                     # data source, design, target-population frame
    eligibility.shared.yaml        # shared selection criteria (optional; objectives may inherit)
    variables.yaml                 # shared variable spec catalog
    shared.lock.yaml               # gate for SHARED data cleaning / base-dataset derivation
  objectives/
    <objective-id>/                # e.g. primary, secondary-process-outcome, ...
      objective.yaml               # question + estimand (type: descriptive | causal | predictive)
      eligibility.yaml             # `inherits: shared` and/or this objective's own criteria
      sap.md                       # THIS objective's SAP (methods-appendix-ready)
      sensitivity.yaml
      population-cascade.yaml       # this objective's target->accessible->sampled->study (own counts)
      deviations.md
      preregistration.lock.yaml    # THIS objective's gate
```

Per-file roles: each `*.lock.yaml` carries `status: draft|locked`, version, `locked_at/by`,
`git_commit`, member checksums, and a completeness summary (counts of `PENDING`). `*.yaml`
spec files mirror the previous schema (estimand fields in `objective.yaml`; selection
criteria in `eligibility*.yaml` with `id` + `excludes_target_population` + `criterion_ref`;
variable catalog fields in `variables.yaml`). All allow `PENDING` /
`PENDING_LOCAL_DECISION` sentinels (mandatory to *pass through*, not to have everything —
but blocking PENDINGs prevent locking that objective).

### 2. Human / agent separation (no contamination)

- `analysis-plan/` is **human-canonical** — what becomes the methods appendix / goes to the
  paper. The agent edits it only to harmonize/fill, never adds its own comprehension notes.
- Agent comprehension artifacts (protocol chunks, derived extractions, RAG indexes, private
  data-profiling) live under **`context/`** (regenerable, gitignored where appropriate) —
  never inside `analysis-plan/`. (Fixes the tsukuba `protocol/derived/`-inside-`protocol/`
  contamination.)
- The lock **checksums** the member files, so a later agent edit to a derived artifact can't
  silently alter the human record without re-locking.
- **Routing:** a "human-only" export ships `analysis-plan/` + `docs/`; the default
  "human+AI" export also includes `context/`. (Reuses the routing/recall layer.)

### 3. Fill-from-arbitrary-inputs (`frame-study` skill)

Drop a protocol / annexes / any inputs → `frame-study` extracts and **harmonizes** them: once
into the `shared/` layer, then **once per objective** into `objectives/<id>/` (each objective
gets its own estimand + SAP + eligibility, inheriting or overriding shared). It **marks
unknowns `PENDING`** and emits a per-target `unresolved-questions` list; it **never invents**
(the tsukuba `<<PENDING_CONFIRMATION_Qn>>` discipline). A completeness report per objective
lists confirmed / pending / blocked; **human sign-off** locks that objective independently.

### 4. The locks + `sap-lock` hook (mandatory, PER OBJECTIVE)

- **Per-objective gating.** Analysis work for an objective lives under a namespaced path
  (`analysis/<objective-id>/…`, outputs `outputs/<objective-id>/…`). The `sap-lock` hook maps
  the write path → objective → checks **that objective's** `preregistration.lock.yaml` is
  `locked`. So a **locked primary advances even while the secondary is draft** — one
  objective never blocks another.
- **Shared base.** Writes to shared data cleaning / base-dataset derivation
  (`analysis/shared/…`, data-onboarding scripts) gate on `shared/shared.lock.yaml`. Each
  objective builds its own cohort on top of that shared base.
- **Graduated strictness — a non-negotiable minimum (hard deny) vs refinable (ask).** Each
  field in `objective.yaml`/`eligibility.yaml`/`variables.yaml` is tagged `tier: core` or
  `tier: refinable`.
  - **`core` (hard `deny`):** the analytical anchor — **exposure/treatment, outcome,
    estimand + contrast, and the target-population frame**. If any core field is `PENDING`,
    writes to that objective's cleaning/analysis paths are **denied** (not merely asked). You
    cannot touch data for an objective whose exposure/outcome aren't fixed (prevents
    outcome-dependent drift).
  - **`refinable` (warn/`ask`):** covariates/adjustment set, data-dependent windows, tuning —
    may stay `PENDING` and **iterate during data handling**; surfaced as a reminder, not a
    block.
- **Two-phase gate per objective:**
  1. **Before data handling / cleaning** (`analysis/<id>/…` writes): `sap-lock` requires the
     **core minimum** non-PENDING → else **deny**. Refinable PENDINGs allowed (iterate).
  2. **Before formal analysis / modeling** (the `data_lock` step): the objective's
     `preregistration.lock` must be `locked` — i.e. **everything** resolved (core +
     refinable) or explicitly `accepted_pending` with justification → else **deny**. "Before
     formal analysis, all of it must be well-defined."
- **Locking** (per file) requires: members present, **no `core` PENDING**, refinable either
  resolved or `accepted_pending`, human sign-off → writes `status: locked` + checksums +
  commit.
- **Gate levels (independent per objective):** `shared.lock` (shared cleaning) → per-objective
  core-minimum (data handling) → per-objective full `preregistration.lock` (formal analysis) →
  `data_lock` (modeling run). Fail-open + opt-in; reads never gated (Invariant 0 — the gate is
  on *writes*, with `deny` reserved for the core-minimum and the locked-before-modeling rules).

### 5. Selection-criteria → flow → cascade wiring (per objective, captured from the start)

- Each objective's `eligibility.yaml` either `inherits: shared` and/or adds its own
  criteria; each criterion carries `id` + `excludes_target_population` + `criterion_ref`.
  Because criteria may vary by objective, **cohort, cascade and flow are per objective** on
  top of the shared base.
- A **per-objective attrition log** (`analysis/<objective-id>/records/attrition_log.csv`)
  accumulates `(step, criterion_ref, n_in, n_out, n_removed, excludes_target_population,
  reason)` — enforced by the **`attrition-log` hook** (a filtering script that doesn't log
  is flagged).
- That objective's `population-cascade.yaml` ties each level's count to its criteria; its
  **flow diagram** (`scaffold-reporting` / `draft-study-flow`) renders from its attrition
  log. Flow inputs are built *during cleaning*, not reconstructed after.
- **`variable-catalog-gate` hook:** a productive script referencing a `status: unknown`
  variable (shared `variables.yaml` or the objective's) is gated (asks).

### 6. Mapping to the decided portfolio

`frame-study` (fill/harmonize + estimand/framework/guideline) · `prespecify-estimand`
(`estimand.yaml`) · `design-indicator` (population/denominator) · `scaffold-reporting`
(flow diagram from the attrition log). New hooks: `sap-lock`, `attrition-log`,
`variable-catalog-gate`. These are domain (`datavidence-healthanalysis`); the gate
*mechanism* may reuse the generic `comprehension_gate`/`routing.yml` engine.

## Consequences

- **Mandatory, auditable pre-registration** with a single machine-checkable gate; human
  appendix stays clean; flow/cascade/variable spine captured from the start; portable.
- **Cost:** friction before analysis — mitigated by the **graduated gate** (hard `deny` only
  on the core minimum — exposure/outcome/estimand/population; `ask` on refinable fields that
  iterate with the data) and by `frame-study` doing the heavy lifting from arbitrary inputs.
- **Stage 2 ready:** `deviations.md` + the lock + `sap.md` map cleanly to an open registry
  later; not built now.
- Supersedes the distributed tsukuba approach; the modular files mirror what tsukuba already
  had (so its `analysis-plan/` content salvages directly — see the rescue manifest).
