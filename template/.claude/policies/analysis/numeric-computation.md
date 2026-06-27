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
  counts as verified only if its seed is set and recorded (see `reproducibility.md`);
  otherwise treat it like mental arithmetic — `unverified`.
- **Reconcile across surfaces.** A number in prose must equal the same number in
  the table or figure it refers to.
