# outputs/ — deliverable contract

Every task produces **one self-contained product** under its own directory:

```
outputs/<slug>/
├── meta.json     # required — machine-readable manifest of this deliverable
├── index.md      # required — human entry point: what this is, how to read it
└── ...           # the actual artifacts (figures, tables, rendered report, data)
```

## Rules (verifiable)

1. **One directory per task.** `<slug>` is lowercase kebab-case
   (`^[a-z0-9]+(-[a-z0-9]+)*$`), unique, and describes the deliverable.
2. **Self-contained.** A reader needs nothing outside `outputs/<slug>/` to
   understand the product. No relative links escaping the directory.
3. **`meta.json` is present and valid JSON** with at least:
   - `slug` — must equal the directory name.
   - `title` — human-readable title.
   - `created` — ISO-8601 date (YYYY-MM-DD).
   - `source_task` — short description / id of the task that produced it.
   - `inputs` — list of paths under `context/` (or external refs) consumed.
   - `artifacts` — list of files in this directory and a one-line purpose each.
4. **`index.md` is present** and links to every artifact listed in `meta.json`.
5. **No scratch.** Intermediate/ephemeral files go in `tmp/`, never here.

## Example `meta.json`

```json
{
  "slug": "survival-km-curves",
  "title": "Kaplan-Meier survival curves by treatment arm",
  "created": "2026-01-15",
  "source_task": "Estimate KM curves and median survival",
  "inputs": ["context/trial-data-dictionary.pdf"],
  "artifacts": [
    { "path": "index.md", "purpose": "Reader entry point" },
    { "path": "km-curves.png", "purpose": "KM plot, all arms" },
    { "path": "median-survival.csv", "purpose": "Median survival table" }
  ]
}
```
