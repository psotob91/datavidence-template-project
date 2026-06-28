# Health-data checklists (run before coding)

Agent-runnable yes/no checks for the `health/` policies. Answer every item explicitly; any
"no" or "unknown" is a **stop** — fix it or return `PENDING_LOCAL_DECISION` (a needed
methodological choice the local protocol/SAP has not made; do not invent it). Generalized from
the Tsukuba EHR/claims policy kit.

## Phenotype comprehension gate (`phenotyping.md`)

- [ ] Algorithm restated in the agent's own words (inclusion + exclusion + time logic)?
- [ ] ≥2 worked examples (≥1 clear positive, ≥1 clear negative), checked criterion-by-criterion?
- [ ] ≥2 counter-examples (boundary/ambiguous cases that separate the rule from intuition)?
- [ ] An ASCII **decision** diagram with every branch and outcome shown?
- [ ] An ASCII **temporal** diagram for each time-based criterion (windows, counts, gaps)?
- [ ] Language traps named (floors vs exact counts; span vs inter-event gap; anchor windows)?
- [ ] Data granularity confirmed (exact day available, or month-only → state machine)?
- [ ] Time-varying states handled (recurrence, transplant/graft-failure, death/transfer)?
- [ ] **Human signed off** that the document matches intent — BEFORE any pseudocode/code?
- [ ] Validation plan stated (PPV/sensitivity, chart review or PheValuator, portability)?

## Code-list / mapping integrity (`code-mapping.md`)

- [ ] Every code set carries source + version + extraction date, frozen for the study?
- [ ] One grouping approach chosen (comorbidity index | phecode/phecodeX | OMOP concept), not mixed?
- [ ] Crosswalk direction stated and mapping loss quantified (e.g. GEM coverage %)?
- [ ] Cleaning sequence applied (char type → trim/upper → ICD-9 zero-pad → dagger/asterisk →
      terminal-X → cascade truncation), in that order?
- [ ] Validation gates reported (% orphan, % unspecified `.9`, % truncated) against thresholds?
- [ ] Packages current (no archived `icd`); versions pinned (`renv.lock`/`requirements.txt`)?
- [ ] Country/system caveats handled (e.g. ICD-10-CM: the `X` in positions 4–6 is a structural
      placeholder for a meaningful 7th character A/D/S — don't strip from the right; Japan codes
      need manual join tables)?

## Denominator integrity (`routinely-collected-data.md`)

- [ ] Denominator defined BEFORE numerator/outcomes/filters?
- [ ] Population frame declared (resident / registered / enrolled / observed person-time / …)?
- [ ] Source system, time scale, entry/exit, geography, and "people with no records" rule stated?
- [ ] Denominator NOT built from an event-only table?
- [ ] Person-time computed by interval overlap (not naïve max−min across the whole history)?

## Numerator / window / episode alignment (`routinely-collected-data.md`)

- [ ] Numerator is an observed-event definition tied to a code list / phenotype (not biological onset)?
- [ ] Each window typed (lookback / washout / clean / confirmation / outcome / risk / grace-gap / eligibility)?
- [ ] Lookback fully inside observable time, else insufficient-lookback flagged?
- [ ] Index date fixed; confirmation classifies without moving time-zero (no immortal time)?
- [ ] Episodes built with sorted+deduped events, allowed gaps, min duration/records, modality
      hierarchy, and post-death/transfer rules?
- [ ] Recurrence model declared (chronic-irreversible / recurrent-acute / episode-based) and
      re-entry handled conservatively (gaps are non-observable)?

## Adversarial review (reject if any is true)

- [ ] Invents columns, codes, or fields not in the data dictionary?
- [ ] Reads "no record" as "no disease/care/event" outside observable time?
- [ ] Builds a population denominator from event-only data?
- [ ] Moves index/time-zero to a future confirmation date without an estimand that says so?
- [ ] Excludes patients based on information observed AFTER time-zero (unless pre-specified)?
- [ ] Silently drops missing/implausible dates instead of flagging them?
- [ ] Calls an unaudited or externally-borrowed algorithm "validated" without a transport check?
- [ ] Cites a paper for a claim it does not actually make?
