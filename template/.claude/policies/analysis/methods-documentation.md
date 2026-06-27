# Methods documentation (written continuously)

Methods are written alongside the analysis, not reconstructed at the end.

## Rules

- **Write as you go**, linked to the pseudocode-first flow.
- **Notation registry.** Keep `docs/analysis/notation.md` with the mathematical
  notation in **LaTeX**; do not break it. The `notation-check` hook (from the
  `datavidence-healthanalysis` plugin) flags methods text whose symbols are absent
  from the registry — add the symbol, don't drop the check.
- **Journal style, extended.** Methods in top biostatistics-journal language
  (fluent statistical prose, **not** code), at methodological-appendix length,
  with LaTeX equations where needed.
- **Extended processing doc.** A biomedical-informatics-style account of data
  processing (pseudocode, validation checks, iterations performed). Both live in
  `analysis/supplement.qmd`.
