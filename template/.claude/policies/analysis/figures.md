# Figures

Publication-quality, accessible result figures (Nature/Science-grade).

## Rules

- **Colorblind-safe palettes.** Categorical → **Okabe-Ito** (`scale_*_okabeito()`; ≤8
  categories — for 9+ use Paul Tol's *muted* palette, don't interpolate Okabe-Ito);
  continuous → **viridis** or **scico** (Crameri). `ggsci`'s journal palettes
  (npg/nejm/lancet/jama) match a journal's look but are **not** guaranteed colorblind-safe.
- **Never rely on color alone** to separate categories — pair it with shape, line style,
  or a direct label. Verify with a **colorblind simulator** (e.g., Coblis /
  `colorBlindness`), not only a grayscale check.
- **Export vector + raster.** Vector (pdf/svg) plus raster **≥300 dpi (line art ≥600 dpi;
  never JPEG — use PNG/TIFF)**. Size to journal columns (single ~89 mm, double ~183 mm).
  Keep fonts legible (mind the minimum size). Inherit a tuned publication theme.
