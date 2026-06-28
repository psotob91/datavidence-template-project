# Health-data companion (worked examples & checklists)

Teaching artifacts for the `health/` policies in `.claude/policies/health/`. Policies stay
short and prescriptive; the detail, worked cases, and runnable checks live here. Present only
in the **health-data** profile.

| File | Use it for |
|---|---|
| `ascii-timelines.md` | The shared plain-text notation for time logic (decision + temporal diagrams). |
| `phenotyping-examples.md` | A full comprehension-gate pass on a real phenotype (maintenance dialysis). |
| `indicator-scenarios.md` | Denominator / window / recurrence scenarios for EHR & claims indicators. |
| `checklists.md` | Agent-runnable yes/no gates to clear before writing pseudocode or code. |

These are **fixtures, not validated algorithms** for your data. Thresholds, code sets, and
data granularity are local decisions — confirm against your protocol/SAP and the cited
sources (`docs/research/health-data-policies-research.md` in the template repo) before use.
