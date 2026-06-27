# Data onboarding

How source data and its documentation enter the project. Pairs with `data/`,
`config.example.yml`, and the `/datavidence-healthdata:onboard-data` skill.

## Rules

- **Copy light, connect heavy/private.** Small datasets → copy into `data/raw/`
  (committed). Heavy, private, or external data → **connect, don't import**:
  point `config.yml` (git-ignored) at its origin; keep `config.example.yml`
  committed. Move the project → fix the path in `config.yml` → it reruns.
- **Never hardcode absolute paths.** Read locations from `config.yml`; resolve
  internal paths with `here`.
- **Place the minimal human documentation.** On onboarding, write the standard
  reproducibility metadata a non-agent health-science project would keep into
  `metadata/`, `contracts/`, `docs/analysis/`. Leave **nothing floating**.
- **Agent material is separate and disposable.** Extra AI-only context lives in
  `_agent_cache/` — never the source of truth.
- **Record provenance.** Source, date, and checksum for every raw input in
  `metadata/`.
