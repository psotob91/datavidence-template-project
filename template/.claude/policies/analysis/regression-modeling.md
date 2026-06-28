# Regression modeling (without regrets)

Avoid the common regression "regrets". Basis: Heinze, Baillie, Lusa, Sauerbrei, Schmidt,
Harrell & Huebner, *Regression without regrets — initial data analysis is a prerequisite
for multivariable regression* (BMC Med Res Methodol 2024;24:178, STRATOS TG2/TG3), plus
TG2 guidance on variable & functional-form selection.

## Rules

- **Do not dichotomize / categorize continuous predictors** to "simplify" — it discards
  information and can mislead. Keep them continuous and model the shape.
- **Model non-linearity explicitly** (restricted cubic splines or fractional
  polynomials), pre-specifying the flexibility — do not assume linearity by default.
- **Continuous *confounders* (causal adjustment): model the shape flexibly too**
  (RCS / fractional polynomials), never dichotomize or coarsely categorize —
  mis-modeling a confounder's functional form leaves **residual confounding** even
  when it is "adjusted for" (Groenwold et al., *CMAJ* 2013; Becher, *Stat Med*
  1992). For a confounder, removing bias outranks interpretability of its shape; if
  categories are unavoidable use ≥5 groups, never a median split.
- **Avoid stepwise / data-driven selection in *any* regression** (it inflates false
  positives and biases estimates); pre-specify predictors and functional forms from
  subject knowledge. When data-adaptive selection is unavoidable, use **penalized
  regression (LASSO / elastic net, CV-tuned)** — not stepwise; if backward elimination is
  unavoidable, use α ≈ 0.157 (AIC-equivalent), not 0.05.
- **Respect sample size**: the simple "10 EPV" rule is outdated — use the Riley criteria
  (`pmsampsize`) for prediction models, and apply **shrinkage / penalization** when
  events-per-variable is low. Do not overfit.
- **Report functional forms and interactions** (pre-specified), with effect estimates
  + confidence intervals.

For collinearity (it matters by goal, not in the abstract) see `collinearity.md`;
for correlated/clustered observations see `correlated-data.md`.

## Sparse data & separation

Small / sparse data break maximum likelihood in two related ways; both can occur
while the model still "runs fine", and the shared remedy is penalization.

- **Sparse-data bias:** with few events per covariate combination — even in large
  data once many covariates are added — ML odds / hazard / rate ratios are biased
  **away from the null** (a point-estimate bias, not just wide CIs). Detect via
  implausibly large ratios, instability when a covariate is added/removed/collapsed,
  and few events per cell — **not** by trusting convergence. Remedy with
  **penalization / weakly-informative priors** (Firth/Jeffreys, or **log-F(1,1)**
  preferred for effect estimation), **do not penalize the intercept**, and report a
  sensitivity analysis over penalty strength. Basis: Greenland, Mansournia & Altman,
  *BMJ* 2016; Greenland & Mansournia, *Stat Med* 2015.
- **Separation / perfect prediction** (a covariate or linear combination predicts the
  outcome perfectly): ML coefficients diverge to ±∞ while the fit may still
  "converge". Detect via exploding coefficients/SEs, fitted probabilities ≈ 0/1, and
  zero cells. Fix with **Firth's penalized likelihood** (`logistf`, `brglm2`; SAS
  `FIRTH`) and use **profile penalized-likelihood CIs / penalized LR tests, not
  Wald**; the same logic covers Cox monotone likelihood. Basis: Firth, *Biometrika*
  1993; Heinze & Schemper, *Stat Med* 2002; Mansournia et al., *Am J Epidemiol* 2018.
  Sparse-data bias and separation are the same small-data pathology — penalization
  addresses both.
