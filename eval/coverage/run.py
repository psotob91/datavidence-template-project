#!/usr/bin/env python3
"""Recall benchmark for the /coverage safety net.

Scores four selection methods against human-validated ground truth and reports
recall / precision / F-beta (beta=2, recall-weighted), the union miss-rate, the
off-route catch-rate, and an inter-lens decorrelation measure. Deterministic and
stdlib-only — the EXPENSIVE part (running the panel) is done separately and its
nominations are recorded in results.json; this script only scores them, so labels
can be corrected and re-scored for free.

Methods compared:
  router    deterministic routing only (recall derived from fixtures' off_path).
  single    one reviewer, no lens.
  majority  policies nominated by >= ceil(L/2)+ (strict majority of L lenses).
  union     policies nominated by >= 1 lens  <-- the recall safety net.

Scoring space is the CONDITIONAL layer only (analysis/ + health/); universal
always-on policies are excluded from ground truth and from nominations.

Usage:
    python run.py --fixtures fixtures.json --results results.json [--catalog catalog.json] [--beta 2]
Exit 0 always (reporting tool); prints a table + JSON summary.
"""
from __future__ import annotations

import argparse
import json
import math
from itertools import combinations
from pathlib import Path


def cond(paths):
    """Restrict to the conditional layer (has a '/', i.e. analysis/ or health/)."""
    return {p for p in paths if "/" in p}


def prf(pred, truth, beta):
    tp = len(pred & truth)
    rec = tp / len(truth) if truth else 1.0
    prec = tp / len(pred) if pred else (1.0 if not truth else 0.0)
    b2 = beta * beta
    denom = b2 * prec + rec
    fb = (1 + b2) * prec * rec / denom if denom else 0.0
    return rec, prec, fb


def jaccard(a, b):
    if not a and not b:
        return 1.0
    u = a | b
    return len(a & b) / len(u) if u else 1.0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixtures", required=True)
    ap.add_argument("--results", required=True)
    ap.add_argument("--catalog", default=None)
    ap.add_argument("--beta", type=float, default=2.0)
    a = ap.parse_args(argv)

    fixtures = json.loads(Path(a.fixtures).read_text(encoding="utf-8"))
    results = {r["id"]: r for r in json.loads(Path(a.results).read_text(encoding="utf-8"))}
    catalog = None
    if a.catalog:
        catalog = {e["path"] for e in json.loads(Path(a.catalog).read_text(encoding="utf-8"))}

    methods = ["router", "single", "majority", "union"]
    agg = {m: {"rec": [], "prec": [], "fb": []} for m in methods}
    decorr = []
    off_total = off_caught = 0
    residual = []          # (task, missed-by-union)
    unknown = set()        # nominated paths not in catalog
    per_task = []

    for fx in fixtures:
        tid = fx["id"]
        truth = cond(fx["ground_truth"])
        off = cond(fx.get("off_path_positives", []))
        res = results.get(tid, {})
        lenses = {k: cond(v) for k, v in (res.get("lenses") or {}).items()}
        single = cond(res.get("single") or [])
        if catalog is not None:
            for s in list(lenses.values()) + [single]:
                unknown.update(s - catalog)

        L = len(lenses) or 1
        counts = {}
        for s in lenses.values():
            for p in s:
                counts[p] = counts.get(p, 0) + 1
        union = {p for p, c in counts.items() if c >= 1}
        maj_thr = L // 2 + 1
        majority = {p for p, c in counts.items() if c >= maj_thr}
        router_tp = truth - off                      # what the router actually surfaces (within truth)

        preds = {"router": router_tp, "single": single, "majority": majority, "union": union}
        row = {"id": tid, "truth": len(truth), "off_path": len(off)}
        for m in methods:
            rec, prec, fb = prf(preds[m], truth, a.beta)
            # router precision is not measured (router FPs are not recorded)
            agg[m]["rec"].append(rec)
            if m != "router":
                agg[m]["prec"].append(prec)
                agg[m]["fb"].append(fb)
            row[m] = round(rec, 3)
        per_task.append(row)

        off_total += len(off)
        off_caught += len(off & union)
        miss = truth - union
        if miss:
            residual.append((tid, sorted(miss)))

        if len(lenses) >= 2:
            js = [jaccard(x, y) for x, y in combinations(lenses.values(), 2)]
            decorr.append(sum(js) / len(js))

    def mean(xs):
        return sum(xs) / len(xs) if xs else 0.0

    print("\n=== Per-task recall ===")
    print(f"{'task':<32} {'truth':>5} {'off':>4} {'router':>7} {'single':>7} {'major':>7} {'union':>7}")
    for r in per_task:
        print(f"{r['id']:<32} {r['truth']:>5} {r['off_path']:>4} "
              f"{r['router']:>7} {r['single']:>7} {r['majority']:>7} {r['union']:>7}")

    print("\n=== Macro-averaged metrics ===")
    print(f"{'method':<10} {'recall':>7} {'prec':>7} {'F-beta':>7}")
    for m in methods:
        rec = mean(agg[m]["rec"])
        prec = mean(agg[m]["prec"]) if m != "router" else None
        fb = mean(agg[m]["fb"]) if m != "router" else None
        ps = f"{prec:>7.3f}" if prec is not None else f"{'n/a':>7}"
        fs = f"{fb:>7.3f}" if fb is not None else f"{'n/a':>7}"
        print(f"{m:<10} {rec:>7.3f} {ps} {fs}")

    print("\n=== Recall safety net ===")
    print(f"off-route positives caught by union: {off_caught}/{off_total} "
          f"({(off_caught/off_total*100 if off_total else 100):.1f}%)")
    print(f"mean inter-lens Jaccard (decorrelation; lower is better): {mean(decorr):.3f}")
    if residual:
        print("\nRESIDUAL FALSE NEGATIVES (missed even by union) — investigate each:")
        for tid, miss in residual:
            print(f"  {tid}: {miss}")
    else:
        print("\nNo residual false negatives: union recall = 1.00 on every task.")
    if unknown:
        print(f"\nWARNING: nominations not in catalog (typos?): {sorted(unknown)}")

    summary = {
        "n_tasks": len(fixtures),
        "macro_recall": {m: round(mean(agg[m]["rec"]), 4) for m in methods},
        "union_recall": round(mean(agg["union"]["rec"]), 4),
        "off_route_catch_rate": round(off_caught / off_total, 4) if off_total else 1.0,
        "mean_inter_lens_jaccard": round(mean(decorr), 4),
        "residual_false_negatives": residual,
    }
    print("\n=== JSON summary ===")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
