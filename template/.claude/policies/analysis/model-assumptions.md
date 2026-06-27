# Model assumptions

Every model's assumptions are checked and the result is reported. Pairs with the
`/datavidence-healthdata:validate-assumptions` skill.

## Rules

- **Check what the model requires:** linear (residuals, linearity,
  homoscedasticity, influence), Cox (proportional hazards: inspect Schoenfeld
  residuals, then `cox.zph`), GLM
  (overdispersion, link), and multicollinearity (VIF) across regressions.
- **Report checked and found.** State what was tested and what was seen.
- **Act on violations.** A violated assumption triggers a remedy or a sensitivity
  analysis — never silence.
