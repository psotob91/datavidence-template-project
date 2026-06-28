# Pre-specification

Decide the analysis before seeing the outcome–exposure association. Pre-specification
reduces researcher degrees of freedom, but its **binding force and form differ by
study type** — strongest for trials, a structured-template norm (not a registration
mandate) for observational work.

> **See also (health-data profile):** `health/reporting-standards.md` — the TARGET guideline when the estimand is causal from observational (target-trial emulation).

## Rules

- **Specify first.** Define the **estimand** — population, outcome, treatment/exposure
  conditions, summary measure, and **intercurrent-event strategy** (ICH E9(R1); naming
  only ITT vs per-protocol is not enough) — plus the analysis, **before examining any
  outcome–exposure association** (not merely before "looking at results"). Record it in
  `docs/analysis/` (analysis plan / SAP).
- **Document deviations.** Post-hoc changes are allowed but must be flagged as
  such — no HARKing, no silent p-hacking.
- **Label analyses** as pre-specified vs. exploratory/post-hoc in reporting.

## Form by study type

The estimand-first rule above is universal; *how* you pre-specify is task-specific.

- **Trials (strongest):** trial registration + a dated **SAP** under the **ICH
  E9(R1)** estimand framework; protocol per **SPIRIT 2013**.
- **Observational:** pre-specify a protocol / analysis plan via a structured template
  — **HARPER** (Wang et al., 2022) or **STaRT-RWE** (Wang et al., *BMJ* 2021) — and
  report per **STROBE / RECORD**. Trial-style *registration* is **contested**, not
  mandatory (*Epidemiology* editors, 2010) — do not present it as required; the
  durable requirement is a pre-specified plan + honest pre-specified-vs-exploratory
  labels.
- **Prediction models:** pre-specify predictors and outcome, and **justify the
  sample size** (Riley et al., *Stat Med* 2019); report per **TRIPOD+AI** (Collins
  et al., *BMJ* 2024).
- **Causal (target-trial emulation):** write the **target-trial protocol first**
  (eligibility, treatment strategies, assignment, follow-up, outcome, estimand,
  analysis) before estimating from observational data (Hernán & Robins, *Am J
  Epidemiol* 2016).
