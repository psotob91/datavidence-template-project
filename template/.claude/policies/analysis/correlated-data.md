# Correlated / dependent observations

The error is **ignoring** dependence (treating correlated rows as independent),
which inflates the effective N and breaks Type I error and CI coverage. A
mixed/multilevel model is **not** the only — or default — fix: once you account for
the dependence, the right tool follows from the **estimand** (marginal vs
conditional) and the correlation mechanism. Basis: Harrell, *RMS* 2nd ed. (2015)
ch. 7 (GLS for longitudinal data) and *BBR* ch. 15; Harrell, "Longitudinal Data:
Think Serial Correlation First, Random Effects Second" (2022); Liang & Zeger,
*Biometrika* 1986 (GEE); Abadie et al., NBER w24003 (2017).

> **Prerequisite:** `analysis/regression-modeling.md` — modeling choices come first.
> **Next-if:** repeated-measures / time-varying treatment → `analysis/longitudinal-data.md` (g-methods, serial-correlation workflow).

## Rules

- **Never ignore dependence.** That — not "failing to use a multilevel model" — is
  the actual error.
- **Choose by estimand:**
  - **Marginal / population-average** (e.g., an RCT's overall treatment effect) →
    **GLS**, **GEE**, or **cluster-robust SEs / cluster bootstrap**.
  - **Conditional / subject-specific** (individual trajectories, variance
    components, partial pooling across many small clusters) → **mixed / multilevel**.
  - For **non-collapsible** measures (OR, HR) the marginal and conditional effects
    differ even with no confounding — state which you report.
- **Continuous longitudinal / serial outcomes — choose by estimand:**
  - **Marginal / population-average** target (e.g. the typical RCT's overall
    treatment effect): **default to GLS** with a time-decaying correlation structure
    (AR(1) / continuous-time AR(1)) via `nlme::gls` / `rms::Gls` — it targets the
    group-level effect, uses standard ML with clean LR χ² tests, checks assumptions
    easily, and avoids the unrealistic exchangeability of a random intercept (Harrell,
    RMS ch. 7). Model **time as continuous** with >3 time points.
  - **Subject-specific** trajectories, **or MAR dropout in a continuous endpoint**:
    prefer **mixed / MMRM** — random effects target individual trajectories, and MMRM
    handles MAR dropout without explicit imputation (see `longitudinal-data.md` and
    `missingness.md`). Random effects are for subject-specific questions, not the
    average-treatment question.
- **GEE / cluster-robust** when you'd rather not model the correlation — accept
  lower efficiency for robustness, but with **few clusters (< ~30–40)** use a
  small-sample sandwich correction (Mancl–DeRouen) or wild cluster bootstrap.
  Whether to cluster at all is **design-driven**, not automatic (Abadie et al. 2017).
- **Reserve mixed / multilevel models** for where they earn their keep: individual
  prediction, variance-component inference, genuine nested hierarchies, or shrinkage
  across many small clusters. Rapidly-repeated *exchangeable* measures (time order
  irrelevant) are the case where a random intercept's assumption actually fits.

For longitudinal IDA and the repeated-measures workflow see `longitudinal-data.md`.
