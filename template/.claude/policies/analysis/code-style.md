# Code style

Analysis code is read by humans first. Optimize for understanding.

> **Prerequisite:** `analysis/incremental-functions.md` — abstract via the gate before styling.

## Rules

- **Tutorial style.** Analysis code reads step by step, like a teaching notebook —
  a human can follow it without prior context. Applies to IDA, cleaning,
  modeling, everything.
- **Comment the "why".** Each script has a header (purpose, inputs, outputs) and
  inline comments explaining intent, not the obvious. Label `.qmd` chunks.
- **Functions only when scaling** (see `incremental-functions.md`); don't
  pre-abstract.
- **Tests in their own files** (`tests/`), never interleaved with analysis.
- **Format & name consistently:** `styler` / `air`; snake_case.
