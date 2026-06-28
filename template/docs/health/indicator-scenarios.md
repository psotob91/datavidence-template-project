# Indicator scenarios — denominators, windows, recurrence (EHR/claims)

Worked scenarios for `routinely-collected-data.md`. Each shows a common way prevalence/
incidence indicators go wrong on routinely-collected data, and the correct reading. Notation:
`ascii-timelines.md`. These are **teaching fixtures**, not your study's rules — the actual
denominator, windows, and recurrence rule are local decisions (`PENDING_LOCAL_DECISION`
until your protocol/SAP fixes them).

## Scenario 1 — denominator: claims enrollment frame vs EHR contact history

Same person, two data sources, different denominators:

```
claims:   ====================================   (enrolled 2015-01 → 2018-12; at risk the whole span)
events:        o           o                       (2 billed encounters)

EHR:      ----o------------o-----------------       (only contacts are observable; no frame)
```

- In **claims**, the person contributes person-time across the whole enrollment span even
  with few events — denominator = enrolled person-time.
- In **EHR**, absence of a contact is **not** absence of disease/care; you cannot treat the
  gaps as at-risk observable time unless a validated registration/list population defines the
  frame. **Define the denominator before the numerator**, and never build a population
  denominator from an event-only table.

## Scenario 2 — washout adequacy (incident / new-user design)

An "incident" case is only incident relative to **observable** prior time. Short lookback
misclassifies prevalent users as incident:

```
GOOD — washout sits entirely inside observable time:
observable:        [================================]
lookback/washout:    [---------------)x                      (whole [---) is within ==== → x is truly incident)

BAD — observable starts late; washout would need unobservable time:
observable:        ?????[=======================]
lookback/washout:    [---------------)x                      ([---) spills into ????? → CANNOT confirm incident)
```

If the washout window is not fully inside observable time, **flag insufficient lookback** —
do not silently call the case incident (Suissa: standard 6–12-month washouts can still leave
a large fraction of prevalent users misclassified). Longer washout trades sensitivity for
specificity; choose and report it.

## Scenario 3 — future confirmation does not move time-zero

A second record confirms the phenotype but the index date stays put (unless the estimand
explicitly targets confirmed survivors — which would induce immortal time):

```
observable:   =========x=============c=====================
index:                 |x                                   (time-zero = first eligible event)
confirm:                            |c                       (classifies as confirmed; does NOT become time-zero)
outcome win:           (-----------------------------------]
```

Moving time-zero to `c` would make everyone between `x` and `c` artificially event-free →
**immortal-time bias**.

## Scenario 4 — recurrence / re-entry across a coverage gap

Repeated patient IDs and gaps need an explicit rule. A gap is **non-observable**, not "no
event":

```
observable:   =========x=====!=====----????----=====x2====!2====
episode 1:             |x...........|                            (event, then disenroll)
gap:                                 ----????----              (NOT at-risk; absence here ≠ no event)
episode 2:                                       |x2.......|     (re-entry: new episode or same?)
```

Declare the recurrence model up front: **chronic irreversible** (one incident event per
person ever), **recurrent acute** (new events allowed after a clean window), or
**episode-based**. Re-entry defaults to conservative: washout does not silently span the gap;
require fresh observable time before counting `x2`.

## Scenario 5 — "no record ≠ absence" (the cross-cutting rule)

```
observable:   ====================o====================
truth?:       only "no observed record in observable time" — NEVER "no disease/care/event"
```

Outside approved observable time, a missing record carries no information about disease,
event, care, or exposure. Phrase findings as observed-record statements, not biological ones.

Before coding any indicator, run the relevant lists in `checklists.md`.
