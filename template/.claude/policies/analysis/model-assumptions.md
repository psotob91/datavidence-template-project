# Model assumptions

Diagnose every model's assumptions, prefer graphics over tests, and explain the
verdict — including when a violation does not actually matter. Pairs with the
`/datavidence-healthdata:validate-assumptions` skill.

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
  - Cox: proportional hazards — inspect **Schoenfeld residuals**, then `cox.zph`.
- **Always check linearity of continuous predictors, outliers, and influential
  points** (e.g., Cook's distance, dfbeta) — pick the best plot for each model
  type. These matter.
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
