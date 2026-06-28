# 0001. Record architecture decisions

Date: 2026-06-28

## Status

Accepted

## Context

The factory has accumulated significant design decisions (the master/child boundary,
the meta-learner loop, the health-data profile, the routing + recall architecture)
that were until now scattered across `learning/`, `SESSION_STATE.md`, commit messages,
and the child's own `template/docs/adr/`. The factory root had no ADR log of its own,
so the *why* behind factory-level decisions was hard to retrieve.

## Decision

We will keep **Architecture Decision Records** for factory-level decisions in
`docs/adr/`, one file per decision, using the lightweight Nygard format
(`# NNNN. Title` / Date / Status / Context / Decision / Consequences). This mirrors the
child's `template/docs/adr/` and satisfies constitution rule 8 (decisions are not loose).

ADRs are immutable once Accepted; a later decision that overrides one is a new ADR that
marks the old one Superseded.

## Consequences

- Factory decisions are retrievable from one place (routed via `.claude/knowledge-map.md`).
- The child already ships its own ADR convention; this brings the factory to parity.
- Minor overhead per decision; acceptable for decisions worth remembering.
