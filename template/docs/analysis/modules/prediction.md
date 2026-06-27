# Module: prediction models

Enabled because `prediction` is in `modules`. For developing / validating clinical
prediction (prognostic or diagnostic) models.

- **Frameworks:** report with **TRIPOD+AI (2024)** (supersedes TRIPOD 2015; regression and
  ML); risk of bias with **PROBAST+AI (2025)**. (PROGRESS-3 is the prognostic-model
  *research strategy* — development, validation, impact — not a reporting guideline.)
- **Method:** pre-specify; check **sample size** (`pmsampsize`); develop; assess
  **discrimination + calibration** (calibration plot / slope / intercept — **Hosmer-Lemeshow
  is deprecated**); **internal validation** (bootstrap optimism correction) and, ideally,
  **external validation**. Apparent (in-sample) performance alone is deprecated. Do not
  interpret coefficients causally.
- **Packages:** `rms`, `pmsampsize`, `tidymodels`/`probably`, `pROC`/`yardstick`.
- Pairs with `analysis/regression-modeling.md`.
