# Verification effort & escalation

Match verification rigor to STAKES, not to what tools are available. Default to
the lightest method that answers the question; escalate only when the cost of
being wrong justifies it. This policy decides HOW MUCH machinery to spend
checking a claim — it never licenses fabrication. `anti-hallucination.md`
outranks it: stay honest and anchored at every tier.

## Tiers

| Tier | Method | Use for |
|------|--------|---------|
| **Light** (default) | A few targeted searches/reads + your own synthesis; tag VERIFIED / OPINION / UNVERIFIED | SOTA scans, orientation, factual lookups, anything you will sanity-check yourself |
| **Medium** | One independent check of only the few claims a decision rests on | Moderate stakes; a couple of contested facts |
| **Heavy** | Multi-vote adversarial verification harness (e.g. the built-in `deep-research`: ~100 agents, each skeptic re-searches the web) | Rare — only under the gate below |

## When the HEAVY tier is allowed (ALL must hold)

Invoke a multi-vote adversarial harness ONLY when every condition is true:

1. **High stakes** — being wrong is costly, irreversible, or outward-facing
   (clinical / legal / financial guidance, a published result, a decision you
   will act on without re-checking).
2. **Contested or extraordinary** — sources conflict, the claim is surprising,
   or there is hype / marketing to filter out.
3. **Decision hinges on it** — the answer materially changes what you do.
4. **No human pass will catch the error** — you will not re-check it yourself.
5. **Budget allows** — confirmed token / time / session headroom. Heavy
   verification with no budget guard can exhaust the session and fail before it
   even synthesizes (an observed failure mode); confirm headroom first.

If any condition is false, stay at Light or Medium.

## Hard "do NOT escalate" triggers

Routine literature / SOTA scans · orientation · factual lookups · exploratory
questions · low-stakes choices · anything you or the user will review anyway.
Heavy adversarial verification on these is waste — and its skeptical default
("refute unless proven") will wrongly kill true-but-hard-to-verify claims.

## Before escalating

State the tier you are about to use and WHY; for the expensive path, **confirm
with the user first** and announce the budget impact. Prefer Medium before Heavy.
