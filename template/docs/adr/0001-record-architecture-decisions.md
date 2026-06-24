# 1. Record architecture decisions

Date: 2026-01-01

## Status

Accepted

## Context

We need a durable, low-ceremony record of the architecturally significant
decisions made on this project: what we chose, when, and why. Without one,
the reasoning behind a decision lives only in people's heads or scattered chat
logs, and is lost when context is compacted or when collaborators rotate.

## Decision

We will use Architecture Decision Records (ADRs), in the lightweight format
described by Michael Nygard.

- Each decision is one Markdown file under `docs/adr/`, numbered sequentially
  and named `NNNN-short-title.md` (e.g. `0002-cowork-plugin-verification-spike.md`).
- Each record has the sections: Status, Context, Decision, Consequences.
- A new record starts from `docs/adr/TEMPLATE.md`.
- ADRs are **immutable** once Accepted. We do not rewrite history. To change a
  decision, write a NEW ADR and set the old one's Status to
  `Superseded by NNNN`. Allowed statuses: Proposed, Accepted, Deprecated,
  Superseded by NNNN.

## Consequences

- The rationale behind every significant decision is discoverable in-repo and
  survives context loss.
- Reviewers and Claude can read `docs/adr/` to understand prior constraints
  before proposing changes.
- There is a small, deliberate cost: a significant decision is not "done"
  until its ADR is written.
