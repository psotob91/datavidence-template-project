# Phenotyping worked example — maintenance dialysis

A complete pass through the **comprehension gate** in `phenotyping.md`, using a real
phenotype: identifying **maintenance (chronic) dialysis** and separating it from
**acute/temporary** dialysis (AKI or acute-on-chronic). Use it as the template for any new
phenotype: restate → examples → counter-examples → ASCII decision diagram → ASCII temporal
diagram → human sign-off → pseudocode → code. Notation: see `ascii-timelines.md`.

> This is a **teaching fixture**, not a validated algorithm for your data. Thresholds,
> codes, and data granularity are local decisions — confirm them against your protocol and
> the cited papers before use.

## 1. Restate the algorithm in plain words

Three published algorithms, chosen by what your data supports. **Verify each citation and its
exact thresholds against the source paper before formal use** — the Lam and Tsunoda
attributions below came from the source conversation and are **not yet confirmed** (no DOI
verified); only Gao et al. 2025 (AJKD 86(2):212–221) has been confirmed.

- **Gao et al. 2025 (AJKD), day-level EHR.** A patient is maintenance-dialysis if **either**
  (1) a CKD-5 (`N18.5`) or ESKD (`N18.6`) diagnosis has a dialysis code **within 7 days**
  (fast-track); **or** (2) there are **≥3 dialysis codes**, the **span from first to last
  code is > 1 month (implemented as > 30 days)**, **and ≥2 codes fall within some rolling
  90-day window**. (Thresholds >7 / >30 / >60 / >90 days were compared; **>30** was selected.
  Reported specificity ≈99.8% in development; ≈99.95% at external validation.)
- **A modality-first approach** (attribution provisional — "Lam et al. 2026, *Kidney
  Medicine*"; confirm before citing). Peritoneal or home hemodialysis → include from day 1;
  in-center hemodialysis → require **> 90 continuous days**.
- **A month-level state machine for masked national data** (attribution provisional —
  "Tsunoda et al. 2022, *Clin Exp Nephrol*"; that paper studies NDB monthly HD trends, so
  treat the state-machine framing as *adapted from* the monthly NDB structure, not a method
  the paper names). HD this month × HD in prior months → prevalent; HD this month × none prior
  → incident; none this month × HD prior → discontinued/death; none × none → not a dialysis
  patient. (Used when exact procedure dates are masked, leaving only year-month.)

**Language traps the restatement must defuse** (these caused 6+ correction cycles in the
source discussion):

- **"3 dialysis codes" = a floor (≥3), not an exact count.** A 3×/week patient has dozens.
- **"lasting longer than a month" = span(last − first) > 30 days**, NOT a required gap
  *between* codes. Read the whole observed block at once.
- **The 90-day window is a recency/density anchor**, not the persistence measure — it stops
  an old acute episode from being read as current maintenance.

## 2. Worked examples (clear positive, clear negative)

**Positive — classic chronic patient (3×/week, 3 months shown):**

```
weeks:   [XXX][XXX][XXX][XXX][XXX][XXX][XXX][XXX][XXX][XXX][XXX][XXX]
(X = a dialysis code in that week)
check:  ≥3 codes? yes (~36)   span > 30 d? yes (~90 d)   ≥2 in a 90-d window? yes
→ INCLUDE (true positive)
```

**Negative — acute kidney injury in the ICU:**

```
weeks:   [XXX][   ][   ][   ][   ][   ][   ][   ][   ][   ][   ][   ]
(3 codes on days 1, 3, 5; patient recovers, no further dialysis)
check:  ≥3 codes? yes   span > 30 d? NO (4 d)   → EXCLUDE (avoids false positive)
```

## 3. Counter-examples (boundary cases that distinguish the algorithm from intuition)

**Counter-example A — the "looks too close at first" trap (PASS).** Once-weekly HD; the
first three codes are only 14 days apart, which *looks* like a fail — but the rule reads the
**entire** block, not the first-to-third gap:

```
weeks:   |- 1 -|- 2 -|- 3 -|- 4 -|- 5 -|- 6 -|
days:       1     8    15    22    29    36
codes:    [o]   [o]   [o]   [o]   [o]   [o]
           |_____________ span = 35 d ________|   > 30 d → INCLUDE
```

**Counter-example B — sparse-but-chronic (PASS).** Monthly peritoneal-dialysis control
visits — only 3 codes in 3 months, but spread out:

```
weeks:   [X ][   ][   ][   ][X ][   ][   ][   ][X ][   ][   ][   ]
days:      1                  29                 57
check:  ≥3 codes? yes   span > 30 d? yes (57 d)   ≥2 in 90 d? yes   → INCLUDE
```

**Counter-example C — early/interrupted chronic (EXCLUDE under Criterion 2, RESCUED by
Criterion 1).** 3 codes over 2 weeks then stops → span < 30 d → would be excluded; **but** if
a CKD-5 (`N18.5`) code sat within 7 days of the first dialysis, the fast-track includes it.
Shows why the two criteria are OR-ed.

**Counter-example D — graft failure / re-entry (time-varying state).** Persistent HD in year
1 → transplant (`Z94.0`) → graft failure (`T86.12`) in year 4 → HD resumes. A naïve
`max(date) − min(date)` spans years and merges distinct episodes. Correct handling:
**segment into episodes at gaps > 90 days**, restart the clock after transplant, classify the
post-failure resumption as a **new incident** maintenance episode.

## 4. ASCII decision diagram (Gao et al.)

```
[Start: evaluate one patient's renal records]
        |
        v
  <CKD-5 (N18.5) or ESKD (N18.6) coded?>
   | yes                              | no
   v                                  v
 <dialysis code within 7 days?>     [go to persistence test]
   | yes        | no
   v            v
 [INCLUDE]   [go to persistence test]

[Persistence test (Criterion 2)]
        |
        v
  <≥3 dialysis codes AND ≥2 within some 90-day window?>
   | yes                              | no
   v                                  v
  <span(last − first) > 30 days?>   [EXCLUDE]
   | yes        | no
   v            v
 [INCLUDE]   [EXCLUDE]
```

## 5. ASCII temporal diagram (the acute vs chronic contrast)

```
day:               1    8   ...                    ~90
chronic (PASS):   |o    o    o    o   ...   o    o|   span ≫ 30 d, dense → INCLUDE
acute   (FAIL):   |ooo                            |   3 codes on days 1–5, span = 4 d → EXCLUDE
                   ^days 1,3,5                  ^day ~90
```

## 6. Pitfalls log (carry into validation & sensitivity)

- Acute-on-chronic: an AKI episode > 30 days can pass Criterion 2 — consider requiring > 90
  days when an AKI code (`N17.*`) is within 14 days of the first dialysis code.
- Inpatient HD has higher prior probability of being acute — profile inpatient vs outpatient.
- Japan: PD/home-HD are essentially always maintenance (acute PD ≈ nonexistent); flag only if
  an AKI code coincides with the first PD code.
- Data granularity decides the algorithm: confirm whether the procedure table holds the exact
  execution day before writing any day-level rule; if only year-month, use the monthly
  state-machine.

Once the human agrees this document matches their intent, hand the criteria to
`pseudocode-first.md`; seed unit tests from these examples and counter-examples (each becomes
an expected-classification fixture — see `checklists.md`).
