# Coverage recall benchmark — results

**Question:** does the `/coverage` ensemble (5 decorrelated Sonnet lenses, aggregated
by **union**) actually prevent false negatives — i.e. catch relevant policies the
deterministic router misses?

**Run:** 10 tasks × (5 lenses + 1 single) = 60 Sonnet agents. Scored by
[`run.py`](run.py) against human-authored ground truth in [`fixtures.json`](fixtures.json)
(re-run: `python run.py --fixtures fixtures.json --results results.json --catalog catalog.json`).
Nominations are frozen in [`results.json`](results.json), so labels can be corrected and
re-scored for free.

## Headline

| method | macro recall | precision | F-β (β=2) |
|--------|:---:|:---:|:---:|
| router only (deterministic) | **0.053** | n/a | n/a |
| single reviewer | 0.958 | 0.327 | 0.678 |
| lens **majority** (≥3/5) | 0.765 | 0.329 | 0.594 |
| lens **union** (≥1/5) ← the safety net | **1.000** | 0.196 | 0.544 |

- **Union recall = 1.000; residual false negatives = 0.** Every relevant policy on
  every task was surfaced.
- **Off-route catch-rate = 46/46 (100%).** Every ground-truth policy the deterministic
  router would *not* have surfaced was caught by the union.
- **Ordering is exactly as designed:** union (1.00) > single (0.96) > majority (0.77) >
  router (0.05). Requiring agreement (majority) *lowers* recall — confirming that union
  is the right aggregation for a recall safety net and majority is a precision move.
- **Decorrelation is real:** mean inter-lens Jaccard = 0.347 (lenses overlap only ~⅓).
  The lenses look at genuinely different things, which is why the union miss-rate
  collapses (≈ pᴺ holds; the lenses did not degenerate into identical sets).

## The recall/precision trade-off (honest)

Union casts a wide net: precision 0.196 — it surfaces ~5× the truly-relevant set. That
is the *intended* cost of a recall-first net and why the design is **two-tier**:
- **Tier-1 (must consult)** = majority vote → precision 0.329, recall 0.765 — the
  confident shortlist.
- **Tier-2 (consider)** = union → recall 1.000 — skim each one-line scope; cheap.
The user reads Tier-1 fully and skims Tier-2; nothing relevant is lost.

## Caveats (do not over-claim)

- **N = 10, single run, fixtures authored in-house.** This is strong evidence the
  mechanism works as designed, not a proof of universal zero-false-negatives. Ground-truth
  labels need **domain-expert validation** (Percy); because nominations are frozen,
  correcting a label only re-runs the free scorer.
- **Off-path positives were engineered** (every task has ≥1 policy the router misses), so
  the router's 0.05 recall is a deliberate stress test, not its typical performance.
- **Universal always-on policies are out of scope** (excluded from ground truth and
  nominations); the benchmark measures the *conditional* layer only.

## Reproduce

```
python run.py --fixtures fixtures.json --results results.json --catalog catalog.json
```
Regenerate `results.json` by re-running the panel workflow (see SESSION_STATE / the
workflow script) — the panel is the expensive step; scoring is instant.
