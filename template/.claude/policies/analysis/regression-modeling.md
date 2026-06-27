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
- **Avoid data-driven / stepwise selection** for explanatory models; pre-specify
  predictors and functional forms from subject knowledge. (Variable selection is a
  *task* decision — it differs for causal vs predictive; see `statistical-reporting.md`.)
- **Respect sample size**: check events-per-variable / required sample size
  (`pmsampsize` for prediction models); do not overfit.
- **Report functional forms and interactions** (pre-specified), with effect estimates
  + confidence intervals.
