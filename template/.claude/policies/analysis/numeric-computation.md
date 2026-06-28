# Numeric computation

Specializes `anti-hallucination.md` for numbers. Outranked only by it: a number
you cannot anchor is not assertable.

## Rules

- **Numbers are claims — never compute them in your head.** Every count,
  percentage, difference, ratio, CI, p-value, or figure/table annotation is
  derived with code (R) or a math tool (WolframAlpha MCP). No mental arithmetic,
  no eyeballed rounding.
- **Every number traces to its code.** A reported value points to the target,
  script, or inline chunk that produced it. If you cannot point to that code, the
  number is `unverified` — mark it, do not assert it.
- **Subagents delegate math.** A subagent reasons about *what* to compute, then
  calls a tool to compute it and cites the result. Reasoning ≠ computing.
- **Stochastic numbers need a seed.** A value from a bootstrap / MCMC / imputation / CV
  counts as verified only if its seed is set and recorded — `set.seed()` + `RNGkind()`,
  and for parallel the **L'Ecuyer-CMRG** streams (`parallel::clusterSetRNGStream` /
  `future.seed = TRUE`) so the result is identical regardless of worker count (see
  `reproducibility.md`); otherwise treat it like mental arithmetic — `unverified`.
- **Exception — equivalence within tolerance when exactness is genuinely impossible.**
  Bit-for-bit reproducibility is the default; only when it cannot hold (different
  BLAS/LAPACK, GPU, cross-platform float, non-deterministic parallel reductions,
  cross-version MCMC) may a number be verified by **numerical equivalence** instead.
  Then **document why**, pin versions/`sessionInfo`, and check against an **explicit,
  reported tolerance**:
  - *Deterministic float* — relative tolerance ≈ **1e-8** (R's `all.equal` default,
    `sqrt(.Machine$double.eps)`), loosened toward ~1e-6 only for heavy / ill-conditioned
    linear algebra.
  - *Stochastic* — agreement **within a few Monte-Carlo standard errors**
    (|Δ| ≤ k·√(MCSE₁²+MCSE₂²); k = 2 routine, 3 strict); **report the MCSE** and raise
    iterations until it is ≪ the effect of interest.

  Basis: Koehler, Brown & Haneuse, *Am Stat* 2009; Morris, White & Crowther, *Stat Med*
  2019. A loosened tolerance is a last resort that can mask bugs — never a blanket default.
- **Reconcile across surfaces.** A number in prose must equal the same number in
  the table or figure it refers to.
