# Module: spatial data

Enabled because `spatial` is in `modules`. For spatial objects / geographic analysis.

- **Method:** keep geometries valid; track the **CRS**; spatial objects can be large →
  apply the regenerables / connect-don't-import rules (`analysis/regenerables.md`,
  `analysis/data-onboarding.md`). Protect precise coordinates — jitter for non-open
  uploads (`analysis/data-protection.md`).
- **Packages:** `sf` (vector), `terra` / `stars` (raster).
