# Module: prediction models

Enabled because `prediction` is in `modules`. For developing / validating clinical
prediction (prognostic or diagnostic) models.

- **Frameworks:** PROGRESS-3; report with **TRIPOD** (+ TRIPOD-AI); risk of bias with
  **PROBAST**.
- **Method:** pre-specify; check **sample size** (`pmsampsize`); develop; assess
  **calibration + discrimination**; **internal validation** (bootstrap optimism
  correction) and, ideally, **external validation**. Do not interpret coefficients causally.
- **Packages:** `rms`, `pmsampsize`, `tidymodels`/`probably`, `pROC`/`yardstick`.
- Pairs with `analysis/regression-modeling.md`.
