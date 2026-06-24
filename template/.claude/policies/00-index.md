# Policies index

Atomic, actionable policies that refine the constitution. Each is short and
self-contained. Open only the one the current task needs.

| Policy                  | One-line scope                                                        |
|-------------------------|-----------------------------------------------------------------------|
| `anti-hallucination.md` | Sentinel values, claim-to-evidence anchoring, no fabricated citations |
| `anti-bias.md`          | Named cognitive biases and concrete counter-moves                     |
| `anti-drift.md`         | Stay anchored to the charter; document hierarchy; size hygiene        |
| `token-efficiency.md`   | Reason expensively, execute cheaply; cascade-first; narrow reads      |
| `verification-effort.md`| Match verification rigor to stakes; gate the heavy adversarial harness |
| `writing-style.md`      | Direct, concrete, scannable, honest, present tense, US English        |

## Precedence (on conflict)

When two policies pull in different directions, the higher one wins:

```
anti-hallucination  >  anti-bias  >  anti-drift  >  verification-effort  >  token-efficiency  >  writing-style
```

Truthfulness outranks everything: never trade accuracy for brevity, style, or a
smaller token bill. The constitution still outranks all policies. When a real
conflict forces a trade-off, stop and name it rather than silently picking one.
