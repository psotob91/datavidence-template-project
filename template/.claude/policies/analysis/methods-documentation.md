# Methods documentation (written continuously)

Methods are written alongside the analysis, not reconstructed at the end.

## Rules

- **Write as you go**, linked to the pseudocode-first flow.
- **Notation registry.** Keep `docs/analysis/notation.md` with the mathematical
  notation in **LaTeX**; do not break it. The `notation-check` hook (in the
  `datavidence-healthanalysis` plugin, PostToolUse) flags methods text whose symbols are
  absent from the registry — keep the
  registry current regardless, and once the hook exists, add the symbol rather than dropping
  the check.
- **Validate the math, not just the rendering.** Distinguish **LaTeX-syntax** validity
  (KaTeX / MathJax error on malformed markup) from **mathematical correctness** (algebra,
  derivations, dimensional consistency). The latter needs a **free symbolic-algebra
  system**: **SymPy** (Python — `pip install sympy`; check with `simplify(lhs - rhs) == 0`
  and its units module) or, in R, **`caracas`** (a SymPy interface). An LLM may *draft* a
  check but **hallucinates on algebra** — always confirm with the CAS.
- **Journal style, extended.** Methods in top biostatistics-journal language
  (fluent statistical prose, **not** code), at methodological-appendix length,
  with LaTeX equations where needed.
- **Extended processing doc.** A biomedical-informatics-style account of data
  processing (pseudocode, validation checks, iterations performed). Both live in
  `analysis/supplement.qmd`.
