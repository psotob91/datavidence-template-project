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
