# Statistical reporting & analysis (by task)

Match methods **and** reporting to the analysis GOAL. General quality steps apply to
every analysis; each task adds its own guideline. Basis: SAMBR (Dwivedi & Shukla, 2020),
SAMPL (Lang & Altman), CHAMP (Mansournia et al., 2021). Reporting guidelines,
risk-of-bias tools, and methodological frameworks are **distinct** — keep them straight.

## General quality steps (all analyses)

Follow SAMBR's **Part B** — a 10-item checklist for the *quality* of statistical analysis
in common study types (design-specific methods are SAMBR Part C):

- Align the analysis with the **design, objective, and hypothesis** before computing.
- Use methods appropriate to design + objective; justify the choice.
- Report **effect sizes with confidence intervals** (not p-values alone); exact p-values
  when used; **name the method and the software + versions**.
- Address confounding / variable selection **as the task requires**.
- Assess **model stability and validity**; interpret with the study's limitations.

## Name the task — it sets the methods and the guideline

- **Descriptive — occurrence/distribution**: characterize, **no causal claims** →
  descriptive-epidemiology framework (Lesko et al., 2022). *Equity/disparities*:
  STROBE-Equity + PROGRESS-Plus. *Overall (fundamental) prognosis* (average outcome in a
  population): PROGRESS-1.
- **Descriptive — relationships / prognostic factor** (a factor's predictiveness,
  bi/multivariable; **not causal**): report with **REMARK**; methodological framework
  PROGRESS-2.
- **Causal / etiologic**: estimand first; target trial emulation + DAGs. Report with
  **STROBE/RECORD** (general observational reporting) **+ TARGET** (the causal/TTE one).
- **Predictive model**: report with **TRIPOD+AI (2024)**; risk of bias with **PROBAST+AI
  (2025)**. (PROGRESS-3 is the methodological strategy for prognostic-model research,
  **not** a reporting guideline.)
- **Diagnostic accuracy**: report with **STARD** (STARD-AI for AI-based tests); risk of
  bias with **QUADAS-2**.
- **Evidence synthesis**: report with **PRISMA**; appraise with **AMSTAR-2** (methodological
  quality) / **ROBIS** (risk of bias). *(module `synthesis`)*

## Self-appraisal lens

- **CHAMP** (CHecklist for statistical Assessment of Medical Papers; Mansournia 2021,
  30 items) is built around the **analytic association / etiologic-causal** paradigm
  (exposure–outcome contrasts, confounding, effect estimates) — its centrepiece (DAG-based
  confounder selection) is causal-analytic, **not** general. Use it as the **primary
  statistical self-appraisal lens for analytic observational studies (cohort / case-control
  / cross-sectional) and RCTs**.
- It is **not** a true all-designs tool (the authors concede each design "has specific
  issues … not covered"). Scope it by task:
  - **Descriptive-only** (no comparison group): apply only CHAMP's task-agnostic items, plus
    the descriptive-epidemiology framework (sampling validity, standardization).
  - **Prediction model** → **TRIPOD** (+ PROBAST); CHAMP's confounder-selection logic
    misleads for predictor selection and it has no calibration/discrimination/validation items.
  - **Diagnostic accuracy** → **STARD** (+ QUADAS-2). **Synthesis** → **PRISMA** + AMSTAR-2/ROBIS.
