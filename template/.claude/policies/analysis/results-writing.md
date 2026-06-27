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
