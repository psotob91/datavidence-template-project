# Outliers

Extreme values are inspected and decided on, never silently removed.

## Rules

- **Pre-specify, then detect → inspect → handle, documenting each step.** Fix the
  detection criteria/thresholds before analysis; never delete a point without a recorded
  reason. Methods: modified Z-score / Grubbs (univariate), Mahalanobis / LOF (multivariate).
- **Distinguish error from signal.** A data-entry error may be fixed or removed (with
  justification); a genuine extreme value is usually kept.
- **Sensitivity is unconditional.** Whenever any value is excluded or modified, run and
  report the analysis **with and without** it — not only when you expect a change.

## By analysis goal

- **Causal:** judge influence **on the effect estimate**, not on fit — **DFBETA /
  standardized DFBETAS for the exposure coefficient** (and Cook's distance). **Never
  drop** an influential point to "clean" the effect; a point that drives the estimate is
  a finding to investigate and **report with/without** as sensitivity. Prefer robust /
  quantile regression over deletion under heavy tails. Pitfall: outlier removal as an
  undisclosed researcher degree of freedom to push the coefficient across significance.
- **Prediction:** judge by impact on **calibration and discrimination**, not residual
  fit. **Winsorizing / transforming predictors** for stability is acceptable (the goal
  is performance, not an unbiased structural coefficient), but **learn the thresholds on
  development data only and freeze them** for deployment (full-sample thresholds leak and
  inflate performance); define out-of-range input handling at deploy time. Basis:
  Steyerberg 2019; Harrell, *RMS* 2015.
- **Description:** for skewed / heavy-tailed data report **robust summaries** (median &
  IQR; trimmed / winsorized means with the fraction stated). Detect with
  distribution-appropriate rules (**MAD-based** z-scores or IQR fences, **not** mean ± k·SD
  — SD is itself distorted by the outliers). Distinguish **data errors** (fix / set
  missing with an audit trail) from **genuine extreme values** (keep — they are part of
  the distribution); **report, don't remove**. Basis: Leys et al., *J Exp Soc Psychol*
  2013; Wilcox 2017.
