# Computational efficiency & resilience

Fast and legible, and never lose hours of compute to a crash.

## Rules

- **Vectorize first.** Prefer vectorized / `data.table` operations over loops; use
  a loop only when it aids readability and under the incremental-functions gate.
- **Right tool for the size.** `data.table` by default; **DuckDB** when data
  exceeds ~½ RAM, lives on disk (Parquet/CSV), or the query is join/aggregation
  heavy. They compose (DuckDB extracts/aggregates → `data.table` models). See the
  `big-data-triage` skill.
- **Parallelize only when it pays** (`future`/`furrr` or `data.table` threads),
  always with reproducible seeds (L'Ecuyer).
- **Don't lose long runs.** Cache and checkpoint expensive compute: `{targets}`
  caches/resumes, Quarto `freeze: true`, intermediate `qs`/`fst` checkpoints.
