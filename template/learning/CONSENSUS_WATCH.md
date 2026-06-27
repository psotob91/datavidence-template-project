# Consensus Watch — methodological standards, frameworks & controversies

A **living radar** of the methodological consensus this project leans on
(reporting standards, evidence frameworks, design principles) **and** the places
where that "consensus" is lagging, contested, or historically wrong. Its job is
not to enforce a dogma but to make our methodological assumptions **explicit,
dated, sourced, and falsifiable** — and to make the agent **flag and ask** rather
than silently obey or silently deviate.

The `UserPromptSubmit` hook captures methodological signals into the queue; the
human-gated `/reflect` skill routes durable ones here.

## Epistemic rules (read before adding or trusting an entry)

1. **Consensus ≠ truth.** A current guideline encodes the field's *present* best
   judgement, which **lags the evidence** and has been wrong before. Cite it,
   date it, note its version — but never treat "the guideline says so" as proof.
2. **Source-anchor, not authority-anchor.** Prefer the primary statement
   (EQUATOR document, GRADE handbook, Cochrane Handbook, the regulator's
   guidance) over a secondary summary. Record which, and the year.
3. **Watch for misconceptions baked into "standard practice"** (see *Known traps*).
   Widespread ≠ correct. The Table 2 fallacy and "adjust for everything" were
   textbook practice for years.
4. **Some questions are legitimately contested** by competent experts (see
   *Contested*). There, present both positions and the trade-off; do **not** pick
   a side as if settled.
5. **Flag, ask, recommend validation — do not act unilaterally.** When the agent
   detects a possible new consensus, a controversy, or a deviation from a standard
   we use, it **surfaces it to the user and recommends how to validate it**; it
   does not silently change an analysis decision or rewrite a method.

## Adopted (standards this project currently follows)

| Standard | Scope | Version / year | Confidence | Re-verify | Source |
|---|---|---|---|---|---|
| STROBE | Observational study reporting | 2007 (+ extensions) | High | every ~12 mo / on new extension | equator-network.org |
| RECORD | Routinely-collected health data | 2015 | High | on update | equator-network.org |
| CONSORT | RCT reporting | 2010 (2025 update landing) | High | confirm 2025 status before citing | equator-network.org |
| TRIPOD (+AI) | Prediction-model reporting | 2015 / TRIPOD+AI 2024 | High | on update | equator-network.org |
| PRISMA | Systematic-review reporting | 2020 | High | on update | prisma-statement.org |
| GRADE | Certainty of evidence / recommendations | living | Med-High | per domain | gradeworkinggroup.org |
| ICH E9(R1) | Estimands & intercurrent events | 2019 | Med | when designing causal/RCT estimands | ich.org |

## Watching (emerging or possibly shifting — do NOT treat as settled)

| Topic | Signal | as-of | Why it may matter | Recommended check |
|---|---|---|---|---|
| CONSORT 2025 | Major update reported | 2026-06 | Changes RCT reporting items we route to | Confirm final 2025/2026 text before citing item numbers |
| Significance reform | Ongoing push to drop "statistically significant" dichotomy / p<0.05 thresholds | 2026-06 | Affects how we phrase inference | Present estimate+interval; avoid bright-line claims unless the user wants them |
| AI/ML reporting | TRIPOD+AI, DECIDE-AI, SPIRIT/CONSORT-AI maturing | 2026-06 | If the project builds models | Re-verify the right checklist per artifact |

## Contested (competent experts disagree — be measured, present both)

- **MCID / minimal clinically important difference.** Useful for interpreting
  effect sizes, but estimation methods (anchor- vs distribution-based) disagree,
  values are population- and instrument-specific, and a single "the MCID" is often
  overstated. Report the effect with uncertainty; treat any MCID as one lens, name
  its source and method, don't anchor a conclusion solely on crossing it.
- **Bayesian vs frequentist.** Both are defensible; the choice changes
  interpretation (posterior probability vs long-run error control), not just
  computation. Prior choice is a substantive, reviewable decision. Don't present a
  Bayesian result as if it answered a frequentist question or vice versa.
- **Estimand framing & causal language in observational work.** The target-trial /
  estimand discipline is increasingly favoured, but how far to push explicit causal
  language without a randomized design is debated. State assumptions; let the user
  set the causal-claim threshold.

## Known traps (documented bad practices to actively avoid)

- **Table 2 fallacy** — interpreting *every* adjusted coefficient in one model as
  a causal effect. Only the estimand's coefficient is interpretable as such; the
  rest are conditional associations (often confounded for the covariate).
- **Confounder ≠ prognostic factor.** They play different causal roles. A variable
  is a confounder *for a specific exposure–outcome relation*; selecting adjustment
  variables by prognostic strength or by p-value (rather than from a DAG) is a
  classic error.
- **Adjusting for mediators or colliders** — conditioning on a mediator removes
  part of the effect; conditioning on a collider opens a spurious path
  (selection/collider bias). Adjustment sets come from the DAG, not from "control
  for everything available".
- **Immortal-time bias** — misaligning eligibility, treatment assignment, and
  follow-up start (especially in routinely-collected-data emulations).

<!-- /reflect appends here from the signal queue. Keep entries dated, sourced, and measured. -->
