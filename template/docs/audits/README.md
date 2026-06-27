# Audits

Durable outputs of multi-agent audits / diagnostics / deep reviews, structured so
they can be re-read cheaply instead of blowing context. See the `/audit-report`
skill for the rules. Each audit is a dated folder:

```
<YYYY-MM-DD>-<slug>/
  00-summary.md   # always-read, bounded synthesis (findings + verdict + decision)
  01-findings.md  # optional detail
  raw/            # optional large sidecars (referenced, never read wholesale)
  INDEX.md        # cheap entry point
```

Read `00-summary.md` first; open the rest only on demand. Route durable lessons
from an audit into `learning/` via `/reflect`.
