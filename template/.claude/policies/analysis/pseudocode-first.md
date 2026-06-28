# Pseudocode first

Agree the approach in words before spending tokens on implementation.

> **Next-if:** repetition warrants abstraction → `analysis/incremental-functions.md`, then `analysis/code-style.md`.
> **See also (health-data profile):** `health/phenotyping.md` — the clinical comprehension gate runs *before* this when defining a phenotype.

## Rules

- **Pseudocode in its own file** before coding a data-management or analysis step
  (in `docs/analysis/` or alongside the step), documented and organized.
- **Validate with the user first**, iterating on the pseudocode.
- **Then** write the real code, and only then add the targeted test.
- Keeps the human in the loop on the *approach* before any complex code exists.
