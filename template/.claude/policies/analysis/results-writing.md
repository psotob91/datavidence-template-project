# Results writing

Results prose is objective and regenerates itself when the data change.

## Rules

- **Objective, no interpretation.** The results section describes what the
  generated tables/figures show; interpretation belongs to discussion.
- **Dynamic by code.** Every number **and every data-dependent word** (top-N
  rankings, "which beats which", direction of an effect) is produced by **inline
  Quarto code**, so it auto-updates when data or analysis change. Nothing
  hardcoded.
- **Numbers come straight from code** (see `numeric-computation.md`).
- **Describe figures from their data.** Use the data that generated a figure to
  describe it; computer vision is only a fallback for reading an already-made one.

## Number formatting (house defaults)

Set once, apply everywhere; consistent with `reporting.md`. Basis: Cole, *Arch Dis
Child* 2015 ("Too many digits"); SAMPL (Lang & Altman 2015); AMA Manual of Style 11th
ed.; ICMJE.

- **Significant figures:** most summary numbers to **2–3 significant figures** (effect
  estimates 2–3; SD/SE 1–2). Precision must reflect uncertainty — don't out-report the SE.
- **Count + percent:** `n (%)`. Percent decimals: **0 if N < 100, 1 if N 100–999, 1–2 if
  N ≥ 1000**; for **n < 20 report counts only**; always give numerator and denominator.
- **Mean (SD):** write `mean (SD)` — **never `mean ± SD`** (AMA: the ± is ambiguous);
  about one decimal beyond the raw measurement; only for ~symmetric data.
- **Median (IQR):** write `median (IQR, P25–P75)` (state the quartiles); decimals match
  the raw data; use for skewed / ordinal data.
- **Range (min–max):** supplementary only — use when the **extremes themselves matter**;
  the default spread is IQR or SD, not the range (it is outlier- and N-sensitive).
- **p-values:** **2 digits if ≥ 0.01, 3 digits if < 0.01, `p < 0.001`** below; exact p
  preferred over thresholds; **never `p = 0.000`**; don't round to flip significance
  (report `0.046`, not `0.05`).
- **Decimal separator: the point** (English artifacts — not the comma, despite local
  Spanish convention); thousands separator consistent throughout.
- **Leading zero:** keep it (`p = 0.03`, `r = 0.42`) unless the target journal mandates
  AMA's no-leading-zero style — decide **once** per project and enforce it.
- **Tables:** decimal-align numbers; identical decimals within a column.
