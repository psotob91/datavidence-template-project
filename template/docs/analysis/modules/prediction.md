# Module: prediction models

Enabled because `prediction` is in `modules`. For developing / validating clinical
prediction (prognostic or diagnostic) models.

- **Frameworks:** report with **TRIPOD** (+ TRIPOD-AI); risk of bias with **PROBAST**.
  (PROGRESS-3 is the prognostic-model *research strategy* — development, validation, and
  impact — not a reporting guideline.)
- **Method:** pre-specify; check **sample size** (`pmsampsize`); develop; assess
  **calibration + discrimination**; **internal validation** (bootstrap optimism
  correction) and, ideally, **external validation**. Do not interpret coefficients causally.
- **Packages:** `rms`, `pmsampsize`, `tidymodels`/`probably`, `pROC`/`yardstick`.
- Pairs with `analysis/regression-modeling.md`.
