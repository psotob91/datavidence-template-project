# context/ — prior domain material (read-only)

This directory holds **input material you bring in**: prior reports, protocols,
data dictionaries, prior analyses, reference papers, domain notes — anything
that informs the work but is NOT produced by it.

## Rules

- **Read-only.** Treat everything here as source-of-truth input. Do not edit,
  reshape, or "tidy" these files; derived work belongs in `outputs/`.
- **Provenance matters.** Prefer keeping original filenames and adding a short
  note (where it came from, date, version) if the source is not obvious.
- **No secrets.** Do not place credentials or restricted data here.

## In Cowork

In a Cowork session, add this material as **"Context"** so it is available to
the assistant without being mistaken for project deliverables.

## Relationship to other folders

- `context/` = inputs (read-only).
- `outputs/` = deliverables produced by tasks (see `outputs/OUTPUT_LAYOUT.md`).
- `tmp/` = ephemeral scratch (gitignored).
