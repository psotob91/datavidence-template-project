# Research — health-data policies (code mapping, phenotyping, EHR/claims indicators)

**Status as of 2026-06-28.** Provenance for three health-data policies added to
`template/.claude/policies/health/`. This file lives at the template-repo root (outside
`template/`), so it is **not** rendered into generated projects — it records *why* the
policies say what they say, and the verified facts behind them. Package availability and
maintenance status drift; **re-verify against CRAN / the upstream repo before relying on
any package name below.**

Source material distilled here:

- `temporal-expansion-ideas/map-codes-health/` — Gemini conversation on CIE-9/CIE-10 →
  phenotype mapping (Peru / Japan / US context).
- `temporal-expansion-ideas/phenotyping-example-dyalisis/` — Gemini conversation building a
  maintenance-dialysis computable phenotype (the worked example shipped to children).
- `methodology-policy-kits/ehr-claims-longitudinal/` (Tsukuba kit) — an agent-navigable
  policy kit on prevalence/incidence from EHR & claims, built on three foundational papers.

---

## 1. Clinical code mapping

### Verified package status (CRAN, 2026-06-28)

| Package | Where | Purpose | Status | Verdict |
|---|---|---|---|---|
| `icd` | CRAN | ICD-9/10 validation, comorbidity maps | **ARCHIVED 2020-10-06** (Rcpp fragility; unmaintained) | **Avoid** |
| `icd.data` | CRAN | data for `icd` | **ARCHIVED** with `icd` | Avoid |
| `medicalcoder` | CRAN | ICD-9/10 lookup/validate + Charlson / Elixhauser / PCCC; longitudinal (present-on-admission + prior-encounter lookback) | **Active**, base-R, dependency-free; first release **2025** (P. DeWitt, CU Anschutz DBMI) | **Prefer** for comorbidity work |
| `comorbidity` | CRAN | Charlson / Elixhauser, ICD-9/10, multiple weightings | **Active**, `icd`-independent (ellessenne / A. Gasparini) | **Use** (mature alternative) |
| `PheWAS` | GitHub `PheWAS/PheWAS` | ICD → phecode mapping + PheWAS | **Active**; **not on CRAN** (install from GitHub) | Use for phecode grouping |
| OHDSI `DatabaseConnector` / `CDMConnector` / `FeatureExtraction` | CRAN + GitHub | OMOP CDM querying & feature/cohort building | **Active** | Use for OMOP/multi-site |

Notes:
- **`icd` is archived** — this was Percy's own premise and is confirmed. Do not introduce it
  into new code; migrate existing code to `medicalcoder` or `comorbidity`.
- **phecodeX** ("Next-generation phenotyping," PMC10627409) is the updated phecode system;
  compatible with the R `PheWAS` package; uses **character prefixes** so R/Excel don't
  corrupt codes by reading them as integers. For international ICD-10 use the
  `*_unrolled_icd10.csv` mapping, not the US ICD-9-CM-biased default.
- **No R package** exists for Japan-specific code systems (DPC, K-codes for procedures,
  YJ-codes for drugs); these require manual join tables against MHLW / KEGG references.

### Frameworks & authorities

- **Diagnosis:** WHO ICD-10/ICD-11; ICD-10-CM (US/CMS, 7-char); GEMs (ICD-9↔ICD-10
  crosswalk, directional); **Phecodes / phecodeX** (Wei Lab, Vanderbilt) for ICD→analyzable
  phenotype grouping; SNOMED CT (SNOMED International).
- **Medications:** RxNorm (NLM), ATC (WHO Collaborating Centre), NDC (FDA).
- **Procedures:** CPT/HCPCS (AMA/CMS, licensed), ICD-10-PCS (CMS), OPCS (UK), ICHI (WHO, new).
- **Labs:** LOINC.
- **Harmonization layer:** OMOP CDM + OHDSI Standardized Vocabularies via **Athena**;
  **UMLS Metathesaurus** (NLM) as the master cross-vocabulary bridge.

### Cleaning sequence (from the source conversation, generalized)

Type-as-character → trim + uppercase → ICD-9 zero-padding (never for ICD-10) → split WHO
dagger/asterisk (etiology/manifestation) → handle terminal `X` carefully → cascade truncation
to the 3-char header block when a full match fails. Then validation gates: report % orphan, %
unspecified (`.9`), % truncated, with WARN/FAIL bands.

Terminal `X`, precisely: in **ICD-10-CM** the `X` in positions 4–6 is a **structural
placeholder** holding the slot for a meaningful **7th character** (encounter type **A/D/S** =
initial/subsequent/sequela) — `X` itself is not the encounter indicator; preserve all
characters and validate against the official tabular list rather than stripping from the
right. Only the **WHO-ICD-10 admin placeholder `X`** (some national extracts, e.g. Peru) is
safe to drop. International caveats: Peru = CIE-10 WHO; Japan = adapted 6-digit blocks +
K-/YJ-codes (no R package).

---

## 2. Computable phenotyping

### Frameworks & consensus

- **Carrell et al. 2024 (JAMIA 31(8):1785–1796, PMID 38748991)** — "A general framework for
  developing computable clinical phenotype algorithms." High-level lifecycle: fitness-for-
  purpose → gold-standard reference data → feature engineering → model development →
  evaluation & reporting; emphasizes scalability and transportability from the start.
- **PheKB / eMERGE** — phenotype authoring + multi-site validation; reported median PPV
  ~96% at authoring site, ~97.5% at implementation sites (portability evidence).
- **OHDSI** — ATLAS (cohort definitions on OMOP), **CohortDiagnostics** (population
  characterization, surfaces misclassification), **PheValuator** (estimates PPV/sensitivity/
  specificity via xSpec/xSens, avoiding exhaustive chart review). APHRODITE (noisy-label ML).
- **Wei et al. 2024 reporting framework (PMC10990558)** — 5 dimensions (not a box-ticking
  checklist): complexity, performance, efficiency, implementability, maintenance.
- **SHREC / PHEONA (2025–2026)** — frameworks for LLM-assisted phenotyping; they treat human
  verification as important but **do not mandate** comprehensive sign-off (SHREC: "encouraged
  but not mandatory"). They establish the *risk* that motivates this factory's comprehension
  gate; the gate is **our** requirement, not their mandate — do not cite them as authority for
  mandatory verification.
- **Validation** = PPV (primary), sensitivity, specificity, NPV; manual chart review (≥2
  reviewers, random + stratified sampling) and/or PheValuator; multi-site for portability.

### The worked example (shipped to children)

Maintenance-dialysis phenotype, from the dialysis conversation. **Only Gao is a confirmed
citation**; Lam and Tsunoda came from the source conversation and are unverified (see caveat
at the end of this section) — the shipped example flags them as provisional.

- **Gao et al. 2025 (AJKD 86(2):212–221; PMC12286722)** — ESKD/maintenance dialysis from EHR.
  Criterion 1 (fast-track): CKD5 (N18.5)/ESKD (N18.6) **with a dialysis code within 7 days**.
  Criterion 2 (persistence): **≥3 dialysis codes**, **span(last − first) > 1 month (>30 days)**,
  **≥2 codes within any rolling 90-day window**. Thresholds explored: >7 / **>30 (chosen)** /
  >60 / >90 days. Reported specificity ~99.8% (development); ~99.95% (external validation).
- **Modality-first (provisional — "Lam et al. 2026, Kidney Medicine"; confirm before use)** —
  PD or home-HD → include from day 1; in-center HD → require **>90 continuous days**.
- **Month-level state machine (provisional — "Tsunoda et al. 2022, Clin Exp Nephrol", which
  studies NDB monthly HD trends; the state-machine framing is *adapted from* the monthly NDB
  structure, not a method the paper names)** — HD this month × HD prior months →
  prevalent / incident / discontinued / none — used when the extract masks exact procedure dates.

Crown teaching point: the phrase "3 dialysis codes lasting longer than a month" is a language
trap. "3" is a **floor (≥3)**, not an exact count; "lasting > a month" is the **span of the
whole set** (last − first > 30 days), **not** a required gap between codes. The 90-day window
is a **recency/density anchor**, not the persistence measure. The classic 3×/week patient has
~72 codes over 6 months and passes trivially; an AKI patient with 3 codes in one week fails.
Episode segmentation (cut at gaps > 90 days) prevents a 2014 acute episode and a 2017 chronic
start being merged into one spurious multi-year "span". Transplant→graft-failure→re-dialysis
must be modeled as a time-varying state (Z94.0 status; T86.12 graft failure) that restarts the
clock. These are exactly the misreadings the comprehension-gate is designed to catch.

---

## 3. EHR/claims prevalence & incidence indicators

### The three foundational papers (from the Tsukuba kit's evidence register)

1. **Bagley SC, Altman RB. 2016. *J Biomed Inform* 63:108–111 (PMID 27498067)** — a
   definitional/conceptual note: introduces "contact" incidence/prevalence and explains that
   EMR disease frequencies reflect **healthcare-seeking patterns** (age, access, insurance),
   so they differ from population-biology measures. (It frames the problem; it does not
   empirically quantify visit-frequency bias.)
2. **Rassen JA, Bartels DB, Schneeweiss S, Patrick AR, Murk W. *Clin Epidemiol* 2019;11:1–15
   (online 2018-12-17; PMID 30588119)** — lookback-window choice dramatically changes estimates
   (all-time vs 1-year lookback: prevalence 4.3–8.3× higher, incidence lower); CPRD + MarketScan,
   5 diseases. (Cite the eCollection year **2019**.)
3. **Spronk I, et al. 2019. *BMC Public Health* 19:512 (PMID 31060532)** — the **major** finding
   is that the **prevalence-type definition** (period vs point vs contact) drives large
   differences (period prevalence ~58–207% higher than point); operational **denominator** choice
   (person-years vs period-average vs mid-period) had only a **slight** effect on incidence rates.

### Extending consensus (verify currency at use)

- **RECORD / RECORD-PE** (STROBE extension for routinely-collected data / pharmaco-epi).
- **ISPOR–ISPE good practices** for real-world-data treatment/effectiveness studies
  (Berger et al. 2017, *Pharmacoepidemiol Drug Saf*).
- **OHDSI / DARWIN-EU `IncidencePrevalence`** R package (standardized estimation on OMOP).
- **Suissa S.** — washout adequacy in the incident-(new-)user design and **immortal-time bias**
  (anchor: Suissa, "Immortal time bias in pharmacoepidemiology," *Am J Epidemiol* 2008;167(4):
  492–499, PMID 18056625); **left-truncation** / delayed-entry bias; new-user active-comparator
  design (Lund et al. 2015).
- **FDA Sentinel** RWE practices; **Book of OHDSI** (cohorts chapter).

### Reusable methodology (from the kit)

EHR vs claims **observability** differ (claims carry an enrollment frame; EHR shows contacts
only unless a validated registration/list population exists). **No record ≠ absence** outside
observable time. **Define the denominator before the numerator.** Eight window types
(lookback, washout, clean, confirmation, outcome, risk, grace/gap, eligibility). Index date
stays fixed; future confirmation classifies but does **not** shift time-zero (unless the
estimand says so). Episodes: sort, dedup at grain, allowed gaps, min duration/records,
modality hierarchy, post-death/transfer rules. Dynamic cohorts: contribute time only while
eligible+observable+at-risk; recurrence/re-entry conservative (gaps are non-observable). The
kit's pseudocode contract (declare grain/keys/source/denominator/windows/recurrence/
missingness/row-counts/validation status) and its `agent_index/` cheap-retrieval pattern are
the model for the future plugin (see the blueprint).

### Shared ASCII timeline notation (adapted from the kit)

`====` observable / at-risk · `----` not-at-risk or non-observable · `|` anchor (index/entry/
exit) · `o` event · `x` index/candidate · `c` confirming record · `!` outcome · `D` death ·
`L` loss-to-follow-up/disenrollment · `?` unobservable gap · `[ ]` inclusive · `( )` exclusive.

---

## Citations (URLs; access at use)

- Carrell 2024 JAMIA — https://academic.oup.com/jamia/article/31/8/1785/7674873 (PMID 38748991)
- Wei 2024 reporting dimensions — https://pmc.ncbi.nlm.nih.gov/articles/PMC10990558/
- phecodeX — https://pmc.ncbi.nlm.nih.gov/articles/PMC10627409/ ; repo https://github.com/PheWAS/PhecodeX
- PheWAS R package — https://github.com/PheWAS/PheWAS
- `medicalcoder` (CRAN) — https://cran.r-project.org/package=medicalcoder
- `comorbidity` (CRAN) — https://cran.r-project.org/package=comorbidity
- OHDSI PheValuator — https://ohdsi.github.io/PheValuator/ ; CohortDiagnostics — https://github.com/OHDSI/CohortDiagnostics
- OHDSI Athena (vocabularies) — https://athena.ohdsi.org/ ; Book of OHDSI — https://ohdsi.github.io/TheBookOfOhdsi/
- Bagley & Altman 2016 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6642638/
- Rassen, Clin Epidemiol 2019 (online 2018) — https://www.tandfonline.com/doi/full/10.2147/CLEP.S181242 (PMID 30588119)
- Spronk 2019 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6501456/ (PMID 31060532)
- Suissa, immortal-time bias, Am J Epidemiol 2008 — https://pubmed.ncbi.nlm.nih.gov/18056625/ (PMID 18056625)
- RECORD/RECORD-PE — https://www.record-statement.org/
- ISPOR–ISPE good practices (Berger 2017) — https://pmc.ncbi.nlm.nih.gov/articles/PMC5639372/
- DARWIN-EU IncidencePrevalence — https://darwin-eu.github.io/IncidencePrevalence/
- Gao 2025 ESKD validation — https://pmc.ncbi.nlm.nih.gov/articles/PMC12286722/

Dialysis-phenotype source papers (Lam 2026 *Kidney Medicine*; Tsunoda 2022 *Clin Exp Nephrol*)
are cited from the source conversation; confirm exact volumes/DOIs before formal use.
