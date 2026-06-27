# Figures

Publication-quality, accessible result figures (Nature/Science-grade).

## Rules

- **Colorblind-safe palettes.** Categorical → **Okabe-Ito** (`scale_*_okabeito()`);
  continuous → **viridis** or **scico** (Crameri, perceptually uniform). `ggsci`'s journal
  palettes (npg/nejm/lancet/jama) match a journal's look but are **not** guaranteed
  colorblind-safe — prefer Okabe-Ito/viridis for accessibility, and always test in grayscale.
- **Never encode meaning by red-vs-green alone.** Pair color with position,
  shape, or a direct label. **Test the figure in grayscale.**
- **Export vector + raster.** Vector (pdf/svg) plus raster ≥300 dpi. Size to
  journal columns (single ~89 mm, double ~183 mm). Keep fonts legible (mind the
  minimum size). Inherit a tuned publication theme.
