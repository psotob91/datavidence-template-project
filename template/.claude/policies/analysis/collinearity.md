# Collinearity (multicollinearity)

Collinearity is not good or bad in the abstract — its relevance depends entirely on
the **estimand**. Variance inflation is confined to the coefficients of the
*mutually collinear* variables; it never touches coefficients you do not interpret,
and (with a fixed model) never touches prediction. Basis: Harrell, *Regression
Modeling Strategies* 2nd ed. (2015); Vatcheva et al., *Epidemiology (Sunnyvale)*
2016; O'Brien, *Qual Quant* 2007; STRATOS (Sauerbrei, Heinze, Harrell et al.,
*Diagn Progn Res* 2020).

## Judge collinearity by the goal

- **Causal / etiologic:** collinearity *among adjustment confounders* does **NOT**
  bias the exposure effect and is not a concern — **never drop a real confounder to
  lower a VIF** (that re-introduces confounding). The only concern is a confounder
  highly collinear **with the exposure itself**: it inflates the exposure's SE and
  is really a **positivity / overlap** signal — inspect overlap and whether the
  contrast is estimable; do not "fix" it by deleting the covariate. (Holds under a
  correctly specified adjustment set.)
- **Prognostic factor (single adjusted association):** assess collinearity **only
  between the factor of interest and its adjusters** (the factor's own VIF /
  partial R²). Collinearity among the *other* adjusters is irrelevant to it. If the
  factor is collinear with an adjuster, report the inflated SE honestly or test the
  correlated group **jointly (multi-df)** — don't delete.
- **Prediction with a FIXED predictor set (no selection):** collinearity does **NOT**
  harm discrimination, calibration, or the predictions — only the individual
  coefficients' interpretability. **Do not remove predictors to reduce VIF.**
  Overfitting / optimism is a **separate** problem driven by complexity vs
  information (predictor count, sample size, events), handled with sample-size /
  shrinkage rules (Riley et al. 2019; van Smeden et al., *Stat Methods Med Res*
  2019) — not collinearity diagnostics. The one real predictive risk: the
  correlation pattern **differs in new data** (extrapolation).
- **Automatic / data-driven selection (stepwise):** here collinearity **is** a real
  problem — correlated predictors compete and the "chosen" one is arbitrary, making
  selection unstable and non-reproducible. Avoid stepwise with correlated predictors
  (see `statistical-reporting.md`, exploratory task); if selection is unavoidable,
  prefer penalized methods and report bootstrap selection frequencies.

## VIF is a flag, not a rule

- VIF is a legitimate diagnostic, but the "**VIF > 10**" (or tolerance < 0.1) cutoff
  is an arbitrary rule of thumb with no firm basis — a high VIF is fully offset by a
  large n (O'Brien 2007). Use VIF to **investigate**, never to auto-delete; read it
  with n, the coefficient's CI, and the condition index / variance-decomposition
  proportions. Tie the response to the goal above, not to the number.
- **Structural** collinearity (polynomials, interactions, splines of the *same*
  variable) is benign — **center** and test the term **jointly (multi-df)**, never
  delete. Only **data-based** collinearity affecting the *focal* coefficient is
  worth acting on.
