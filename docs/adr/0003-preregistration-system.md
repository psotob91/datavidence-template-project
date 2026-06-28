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

Ship a **modular `analysis-plan/` folder gated by a single `preregistration.lock.yaml`**,
filled by the `frame-study` skill and enforced by a `sap-lock` hook. The folder is
**human-canonical** (paper-ready); agent comprehension artifacts live separately under
`context/`. Renders only when `analysis_stack == 'r'` (health-data adds eligibility/
phenotype nuance).

### 1. Folder structure (`template/analysis-plan/`, rendered into the child)

| File | Holds | Layer |
|---|---|---|
| `preregistration.lock.yaml` | **The gate.** `status: draft\|locked`, version, `locked_at/by`, `git_commit`, member-file checksums, completeness summary (counts of `PENDING`). | machine |
| `estimand.yaml` | Target population, contrast, outcome, adjustment set, **estimand type** (descriptive / causal / predictive), explicit non-causal declaration when applicable. | human |
| `objectives.yaml` | Primary + secondary objectives, each tied to an estimand. | human |
| `eligibility.yaml` | **Selection criteria** — each inclusion/exclusion with `id`, text, `excludes_target_population` (bool), `criterion_ref` (links to the attrition log + flow node). *The spine.* | human |
| `population-cascade.yaml` | target → accessible → sampled → study, each level **defined** + a slot for the **count** (filled at runtime from the attrition log). | human |
| `variables.yaml` | Variable spec catalog: `variable_id, analytic_role, source_table, source_column_or_code_set, grain, derivation, qc_rule, status, provenance`. *Variable definitions from the start.* | human |
| `sap.md` | The narrative SAP (methods-appendix-ready prose). | human |
| `sensitivity.yaml` | Pre-specified sensitivity analyses (with source refs). | human |
| `deviations.md` | Append-only deviations log (Stage-2-ready). | human |

All files allow `PENDING` / `PENDING_LOCAL_DECISION` sentinels (mandatory to *pass through*,
not mandatory to have everything — but blocking PENDINGs prevent locking).

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

Drop a protocol / annexes / any inputs → `frame-study` extracts and **harmonizes** them into
the modular files, **marking unknowns `PENDING`** and emitting an `unresolved-questions`
list. It **never invents** (the tsukuba `<<PENDING_CONFIRMATION_Qn>>` discipline). A
completeness report lists confirmed / pending / blocked; **human sign-off** advances status.

### 4. The lock + `sap-lock` hook (the mandatory gate)

- **Locking** requires: all member files present, no *blocking* PENDING (or explicitly
  `accepted_pending`), human sign-off → writes `status: locked` + checksums + git commit.
- **`sap-lock`** (PreToolUse, opt-in via `routing.yml`/config, fail-open): on writes to
  cleaning/analysis paths (`analysis/**`, `R/**`, data-derivation scripts), if the lock is
  not `locked` → **ask** (Invariant 0: additive to reads; only gates writes; asks, never
  hard-denies). File-existence + status check — the most reliable pattern in tsukuba
  (`data_lock.json`).
- **Two distinct gates:** `preregistration.lock` (before cleaning/analysis) and the existing
  `data_lock` (before modeling).

### 5. Selection-criteria → flow → cascade wiring (captured from the start)

- `eligibility.yaml` criteria carry `id` + `excludes_target_population` + `criterion_ref`.
- The attrition log (`analysis/records/attrition_log.csv`) accumulates `(step, criterion_ref,
  n_in, n_out, n_removed, excludes_target_population, reason)` — enforced by the
  **`attrition-log` hook** (a filtering script that doesn't log is flagged).
- `population-cascade.yaml` ties each level's count to the criteria; the **flow diagram**
  (`scaffold-reporting` / `draft-study-flow`) renders from the attrition log. So flow inputs
  are built *during cleaning*, not reconstructed after.
- **`variable-catalog-gate` hook:** a productive script referencing a `status: unknown`
  variable in `variables.yaml` is blocked (asks).

### 6. Mapping to the decided portfolio

`frame-study` (fill/harmonize + estimand/framework/guideline) · `prespecify-estimand`
(`estimand.yaml`) · `design-indicator` (population/denominator) · `scaffold-reporting`
(flow diagram from the attrition log). New hooks: `sap-lock`, `attrition-log`,
`variable-catalog-gate`. These are domain (`datavidence-healthanalysis`); the gate
*mechanism* may reuse the generic `comprehension_gate`/`routing.yml` engine.

## Consequences

- **Mandatory, auditable pre-registration** with a single machine-checkable gate; human
  appendix stays clean; flow/cascade/variable spine captured from the start; portable.
- **Cost:** friction before analysis — mitigated by `PENDING` markers and *ask* (not deny),
  and by `frame-study` doing the heavy lifting from arbitrary inputs.
- **Stage 2 ready:** `deviations.md` + the lock + `sap.md` map cleanly to an open registry
  later; not built now.
- Supersedes the distributed tsukuba approach; the modular files mirror what tsukuba already
  had (so its `analysis-plan/` content salvages directly — see the rescue manifest).
