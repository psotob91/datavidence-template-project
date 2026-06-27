# Notation registry (LaTeX)

The single source of truth for mathematical notation. Methods text
(`analysis/supplement.qmd`, reports) must use **only** symbols declared here — the
`notation-check` hook (from the `datavidence-healthanalysis` plugin) flags any
symbol that is missing. Add the symbol here rather than dropping the check.

Keep it consistent: one symbol, one meaning, across the whole project.

| Symbol (LaTeX) | Meaning |
| --- | --- |
| `$Y_i$` | outcome for unit *i* |
| `$X_i$` | exposure / primary predictor for unit *i* |
| `$Z_i$` | covariate vector for unit *i* |
| `$\beta$` | regression coefficient(s) |
| `$\theta$` | the target estimand |
| `$n$` | analytic sample size |

<!-- Add rows as the analysis introduces notation. Do not redefine a symbol. -->
