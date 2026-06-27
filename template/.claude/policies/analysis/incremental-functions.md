# Incremental functions (STOP-and-confirm gate)

A **strict** gate. Do not skip the steps. Reinforces the constitution's
propose-then-confirm for any abstraction over data/analysis.

## Rules

- **Abstract only when repetition warrants it** — never "just in case".
- **Own file + roxygen2.** Each function in its own file under `R/`, documented;
  its test/demonstration in a **separate** file.
- **Demonstrate before abstracting.** First do the operation **without** the
  function on one case and show it works; then wrap it and show it matches.
- **Loops last.** Show **one** iteration first (the outside, then the inside
  *without* the loop), validate the black box, and only then scale to iterate.
- **HARD CHECKPOINT — STOP and ask.** At this point: stop, ask, build the small
  one-case version, get approval, **then** scale. Never proceed without that
  feedback. The point is that the user sees and understands before tokens go into
  complex code.
