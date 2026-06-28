# Clinical tables (Table 1 / Table 2)

Health-paper tables that honor the base reporting policy (`analysis/reporting.md`).

> **Next-if:** tables assembled for the manuscript → `health/reporting-standards.md` (map to the EQUATOR checklist).

## Rules

- Build with **`gtsummary`** (regression tables via `tbl_regression`), **labels-first**
  (legible names, never code/variable names).
- **No p-values** in descriptive / group-comparison tables unless explicitly requested;
  for causal balance use **standardized differences (SMD)**, not p-values.
- Show **missingness** per variable; report denominators.
- Estimates carry **confidence intervals**; rounding is consistent.
- Emit one **machine-readable** (csv) + one **human-readable** (html/docx) version per
  table (see `outputs/OUTPUT_LAYOUT.md`).
