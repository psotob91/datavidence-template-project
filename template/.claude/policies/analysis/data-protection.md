# Data protection

Keep identifiable data out of everything that travels or is shared.

## Rules

- **No identifiable data in git, `outputs/`, `context/`, or the prompt.** Connect
  private/PII/PHI data via `config.yml` (git-ignored); do not copy it into the
  repo or paste it into a message.
- **Avoid re-identification.** Do not export tables/figures that could
  re-identify individuals (e.g., very small cells). Disclosure-control thresholds
  and methods are project-specific — clinical specifics come with the health-data
  profile.
- **Secrets are separate.** `.env` / keys are blocked by the plugin's
  `env_protect` hook; this policy is about **datasets**.
