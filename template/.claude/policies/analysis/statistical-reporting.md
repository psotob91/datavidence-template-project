# Statistical reporting & analysis (by task)

Match methods **and** reporting to the analysis GOAL. General rules apply to every
analysis; each task adds its own (per-task frameworks below; clinical reporting
standards live in the health profile). Basis: SAMBR (Dwivedi et al., 2020), SAMPL
(Lang & Altman), CHAMP (Mansournia et al., 2021).

## General — applies to all tasks (SAMBR Part B)

- Align the analysis with the **design, objective, and hypothesis** before computing.
- Use **evidence-based methods** appropriate to design + objective; justify the choice.
- Report **effect sizes with confidence intervals** (not p-values alone); give exact
  p-values when used; **name the method and the software + versions**.
- Address confounding / variable selection **as the task requires** (it differs by goal).
- Assess **model stability and validity**; interpret with the study's limitations.

## Name the task — it changes the methods and the guideline

- **Descriptive** (occurrence/distribution; disparities/equity): characterize, **no
  causal claims**. → descriptive-epidemiology framework (Lesko et al., 2022);
  PROGRESS-1; equity: STROBE-Equity + PROGRESS-Plus.
- **Descriptive — relationships / prognostic factor** (a factor's predictiveness,
  bivariable or multivariable; **not causal**): PROGRESS-2; REMARK.
- **Causal / etiologic**: estimand first; **target trial emulation**; confounding via
  DAGs; report with STROBE/RECORD + TARGET. *(module `causal`)*
- **Predictive model**: report with **TRIPOD**, risk-of-bias with **PROBAST**;
  PROGRESS-3. *(module `prediction`)*
- **Diagnostic accuracy**: STARD; risk-of-bias QUADAS-2.
- **Evidence synthesis**: PRISMA; risk-of-bias AMSTAR-2 / ROBIS. *(module `synthesis`)*

## Self-appraisal lens

- Appraise the analysis with **CHAMP** (statistical-assessment checklist for analytic
  studies). Mark items **N/A** by design. CHAMP is **not** the right primary lens for
  descriptive-only work (use the descriptive-epi framework), prediction-model bias
  (use PROBAST), or synthesis (use AMSTAR-2 / ROBIS).
