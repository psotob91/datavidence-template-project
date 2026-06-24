# Token efficiency

Spend reasoning where it pays; never spend it on work a machine can do cheaper.
This policy never overrides truthfulness — accuracy first, then efficiency.

## Principles

- **Reasoning model thinks, cheap executor executes.** Use expensive reasoning
  for judgment, design, and verification. Push mechanical, deterministic work
  down to scripts, hooks, and the executor layer.
- **Cascade-first.** Code distills; the model reasons over the distillation.
  Filter, aggregate, and summarize with a script, then reason about the small
  result — do not pour raw bulk into the context window.
- **Narrow reads.** Read the specific lines, function, or section the task
  needs. Avoid whole-file and whole-directory reads when a slice will do.
- **Batch.** Group independent reads, searches, and edits into one pass instead
  of many round-trips.
- **Mechanical work to hooks / scripts.** Formatting, indexing, validation, and
  reindexing belong in `make` targets and the companion plugin's hooks — not in
  hand-written model output.
- **Structured output.** Prefer compact, structured results (tables, JSON,
  field lists) over prose when a caller or another step will consume them.

## Anti-pattern

Re-reading a file you already hold, restating context you already have, or
loading the corpus "just in case". If you did not need it for this step, do not
load it.

## See also

`verification-effort.md` — the deliberate exception: when a high-stakes,
contested claim justifies spending on the expensive verification path.
