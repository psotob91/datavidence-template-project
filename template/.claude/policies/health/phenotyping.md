# Computable phenotyping (comprehension gate before code)

A computable phenotype turns codes/labs/meds/time into a yes/no (or state) label for a
condition. Getting it wrong silently corrupts every count, model, and conclusion downstream —
so the agent must **prove it understands the algorithm before writing any code**. This policy
extends `analysis/pseudocode-first.md` with a clinical comprehension gate that runs **first**.

## The comprehension gate (mandatory, in order)

Do all of these and get **human sign-off** before pseudocode or code. No exceptions — even a
"simple" single-code phenotype hides assumptions.

1. **Restate** the algorithm in your own words: inclusion criteria, exclusion criteria, and
   the **time logic** (windows, counts, gaps, ordering). Name the **language traps** —
   floors vs exact counts ("≥3" ≠ "exactly 3"), span(last − first) vs gap-between-events,
   anchor windows vs persistence measures.
2. **Worked examples — ≥2** (at least one clear positive, one clear negative), walked
   **criterion by criterion**.
3. **Counter-examples — ≥2**, each exercising a **different boundary** (e.g. one on the count
   threshold, one on the time window, one on an OR-criterion rescue) — not two variants of the
   same failure. Use cases where the algorithm's answer differs from naïve clinical intuition;
   explain the sensitivity/specificity trade-off each exposes.
4. **ASCII decision diagram**: every branch and terminal outcome explicit.
5. **ASCII temporal diagram**: one per time-based criterion (use the shared notation in
   `docs/health/ascii-timelines.md`). If you cannot draw the rule on a timeline, you do not
   understand it well enough to code it. (If a phenotype genuinely has **no** time logic — a
   pure single-code "ever" definition — state that explicitly instead of drawing an empty
   timeline.)
6. **Human sign-off**: the human confirms the restatement + diagrams match intent. **Iterate**
   until aligned. Sign-off is an **explicit affirmative** in the conversation — silence or
   absence of objection is **not** consent. Only then proceed.
7. **Then pseudocode** (`analysis/pseudocode-first.md`), **then code + unit tests** seeded from
   the examples and counter-examples (each becomes an expected-classification fixture).

A full worked pass (maintenance dialysis) lives in `docs/health/phenotyping-examples.md`; the
gate itself is the checklist in `docs/health/checklists.md`.

## Rules

- **Data granularity dictates the algorithm.** Confirm whether the source has the exact event
  **day** before writing any day-level rule; if only **month** is available (e.g. masked
  national extracts), use a **monthly state machine**, not a day-level span.
- **Model time-varying states explicitly.** Recurrence, transplant → graft-failure →
  re-dialysis, death, and transfer restart or end episodes. Segment timelines into episodes
  at declared gaps; never let `max(date) − min(date)` merge distinct episodes.
- **Borrowed algorithms are not validated for your data.** An externally published phenotype
  needs a **transportability check** before you call it validated (`PENDING_LOCAL_DECISION`
  on thresholds/codes until the protocol fixes them).
- **Validate and report.** Estimate **PPV (primary), sensitivity, specificity** via chart
  review (≥2 reviewers; random + stratified sampling) and/or OHDSI **PheValuator** /
  **CohortDiagnostics**; check **portability** across sites/time. Report per the 5 dimensions
  of Wei et al. 2024 (complexity, performance, efficiency, implementability, maintenance).
- **LLM-assisted phenotyping carries classification risk** (SHREC/PHEONA, 2025–2026); this
  factory **requires** the comprehension gate above as its human-verification step — an LLM
  may draft, but never self-certify.
- **Never reify a phenotype** as a true biological subgroup; it is an operational definition
  with measurement error. Carry that error into sensitivity analysis (`sensitivity-analysis.md`).

Framework basis (see `docs/research/health-data-policies-research.md` for citations/URLs):
**Carrell et al. 2024 (JAMIA)** general framework; **PheKB / eMERGE** authoring + multi-site
validation; **OHDSI** ATLAS / CohortDiagnostics / PheValuator; **Wei et al. 2024** reporting.
Pairs with `code-mapping.md`, `secondary-data.md`, `routinely-collected-data.md`,
`analysis/pseudocode-first.md`, and `analysis/diagrams.md`.
