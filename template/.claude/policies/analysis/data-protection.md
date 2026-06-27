# Data protection

Simple rule: the data stays put, and nothing identifiable leaves the project
unless you ask. No modeling around the data, no altering the source to "protect"
it.

## Rules

- **Data lives on your machine; the agent may read it.** Do not copy or transform
  the source for protection's sake.
- **Nothing leaves unless you explicitly ask.** Never push data to git,
  `outputs/`, an upload, or an external service unless you request it (e.g., open
  data you ask to publish).
- **No real identifier columns in anything exported.** Drop them, or replace with
  an anonymized key (add one if rows need an identifier). Nothing more elaborate.
- **Before uploading non-open data, warn me and propose light anonymization of the
  exported copy only** (never the source): e.g., randomly shift the index date,
  jitter precise latitude/longitude. If the data is already open, skip it.
- **Secrets are separate.** `.env` / keys are blocked by the plugin's
  `env_protect` hook; this policy is about datasets.
