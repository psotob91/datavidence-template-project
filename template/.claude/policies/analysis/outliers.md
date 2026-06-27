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
