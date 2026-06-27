# Module: causal inference

Enabled because `causal` is in `modules`. For etiologic / causal questions.

- **Frameworks:** target trial emulation (Hernán & Robins); transparent reporting with
  the **TARGET** statement. Quasi-experiments / natural experiments fit this framing.
- **Method:** define the **estimand**; draw a **DAG** (`dagitty` / `ggdag`) → derive the
  adjustment set; emulate the target trial; run sensitivity analyses / negative controls.
- **Packages:** `dagitty`, `ggdag`, `marginaleffects`, `WeightIt`, `MatchIt`, `survival`.
- Pairs with `analysis/statistical-reporting.md` (causal task) and `analysis/regression-modeling.md`.
