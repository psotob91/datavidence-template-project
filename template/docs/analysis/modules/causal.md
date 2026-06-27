# Module: causal inference

Enabled because `causal` is in `modules`. For etiologic / causal questions.

- **Frameworks:** target trial emulation (Hernán & Robins); transparent reporting with
  the **TARGET** statement. Quasi-experiments / natural experiments fit this framing.
- **Method:** specify the **estimand** (incl. intercurrent-event strategy, ICH E9(R1));
  draw a **DAG** (`dagitty` / `ggdag`) → adjustment set; emulate the target trial — align
  eligibility, assignment, and follow-up start to **avoid immortal-time bias**; state the
  identifying assumptions (exchangeability, positivity, consistency); run sensitivity
  analyses / negative controls.
- **Packages:** `dagitty`, `ggdag`, `marginaleffects`, `WeightIt`, `MatchIt`, `survival`.
- Pairs with `analysis/statistical-reporting.md` (causal task) and `analysis/regression-modeling.md`.
