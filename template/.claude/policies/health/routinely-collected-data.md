# Routinely-collected data — handling & indicators (STUB)

> **STUB — to be completed** from a research brief (left in `temporal-expansion-ideas/`,
> currently being finalized). Scope: **safe, efficient handling of longitudinal
> routinely-collected data** (EHR, claims, surveillance, health-services/management,
> registries) and **indicator construction** (numerators/denominators, time windows).

## Scope (to flesh out)

- **Time done right**: index date; lookback / washout / follow-up **windows**;
  eligibility/enrollment **continuity** (claims); avoid **immortal-time bias** and date
  errors (the easiest mistake to make with time).
- **Numerator / denominator**: person-time, eligibility windows, population at risk; the
  **multiple ways** to build an indicator — document the chosen one and why.
- **Efficient & safe code**: `data.table` / `duckdb` for temporal joins and windowed
  aggregation; assert no overlaps/duplicates; reconcile counts (see `data-integrity.md`,
  `computational-efficiency.md`).
- **EHR vs claims (and beyond)**: claims = billing/eligibility/encounters (coding bias;
  gaps outside coverage); EHR = clinical records/labs/notes (informative presence;
  irregular measurement); surveillance/registries have their own quirks.

Pairs with `secondary-data.md` (RECORD) and `analysis/longitudinal-data.md`.
