# Model assumptions

Diagnose every model's assumptions, prefer graphics over tests, and explain the
verdict — including when a violation does not actually matter. Pairs with the
`/datavidence-healthanalysis:validate-assumptions` skill.

## Rules

- **Graphics over tests.** Prefer diagnostic plots to formal tests. If a test is
  reported anyway, **always add a caveat**: tiny samples pass almost anything,
  huge samples flag trivial deviations — significance ≠ relevance.
- **Use the residual that actually reveals the fit:**
  - Linear: residuals-vs-fitted, scale-location, QQ.
  - GLM / GAM / GAMLSS: **randomized quantile residuals** (Dunn–Smyth;
    `statmod::qresid`) — raw / Pearson / deviance residuals mislead for discrete
    or non-normal responses.
  - Mixed / multilevel: simulation-based scaled residuals via **`DHARMa`**.
  - Cox: proportional hazards — inspect **Schoenfeld residuals**, then `cox.zph`; if
    violated, use a **time-varying coefficient, stratified Cox, or landmark analysis**.
- **Bayesian models are checked differently — convergence/approximation is a
  prerequisite, not a robustifiable assumption:**
  - MCMC: require **R-hat < 1.01** (≥4 chains), **bulk- and tail-ESS ≳ 400**, and clean
    trace plots. **HMC/NUTS (Stan/`brms`)** additionally: investigate and ideally
    eliminate **divergent transitions** — aim for zero (raise `adapt_delta`,
    reparameterize, or revise the model); never report a posterior with unresolved
    divergences. Watch **E-BFMI / treedepth** (Gibbs samplers like JAGS have none). Then
    **posterior predictive checks** (`pp_check`), **prior-sensitivity**, and LOO/WAIC with
    **Pareto-k** for influence.
  - INLA (latent Gaussian models): check **PIT** (≈ uniform) and **CPO** (+ its
    failure flags / `inla.cpo`), the **KLD** column for Laplace-approximation validity;
    use **PC priors** as the principled default, and run prior sensitivity by comparing
    against alternative priors.
  - **No escape hatch here.** Unlike a robust-SE patch, you cannot "robustify" a
    non-converged chain or an invalid approximation. Fix the model — non-centered
    parameterization, better priors, more iterations / higher `adapt_delta`, or a
    different likelihood (for INLA: change strategy or switch to MCMC). **Never
    report a posterior from a non-converged fit.**
- **Always check linearity of continuous predictors, outliers, and influential
  points** (e.g., Cook's distance, dfbeta). On non-linearity, **model it (restricted
  cubic splines / fractional polynomials) — never dichotomize** (see
  `regression-modeling.md`). Pick the best plot for each model type.
- **A violated assumption does NOT invalidate the model.** Many models are robust
  to some deviations — say so, with a comment, when that is reasonable. **Educate
  the user every time**; never assume they know why it does or doesn't matter.
- **Know what a "fix" actually fixes:**
  - A robustness patch (robust/sandwich SE, cluster-robust) makes the *patched*
    model's **inference** valid but does **not** change the naive fit — its
    residuals still look off. Say this explicitly.
  - Some adjustments correct the **fit** itself (e.g., WLS for heteroscedasticity,
    a better link / family / transform). Then judge success with the residual
    that reveals the correction (weighted/standardized residuals for WLS;
    randomized quantile residuals for GLMs).
- **Comment every diagnostic and every remedy** so the reader learns the *why*.
