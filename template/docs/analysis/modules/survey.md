# Module: complex survey design

Enabled because `survey` is in `modules`. For weighted / stratified / clustered samples
(e.g., ENDES, DHS, national health surveys).

- **Method:** declare the design (**weights, strata, clusters**) once and use
  **design-based estimation** throughout; report design-adjusted estimates with CIs.
  Mind subpopulation (domain) estimation — subset *within* the design object.
- **Packages:** `survey`, `srvyr`.
