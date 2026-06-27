# Figures

Publication-quality, accessible result figures (Nature/Science-grade).

## Rules

- **Colorblind-safe palettes.** Categorical → **Okabe-Ito**
  (`scale_*_okabeito()`) or a journal palette (`ggsci`: npg/nejm/lancet/jama);
  continuous → **viridis** or **scico** (Crameri, perceptually uniform).
- **Never encode meaning by red-vs-green alone.** Pair color with position,
  shape, or a direct label. **Test the figure in grayscale.**
- **Export vector + raster.** Vector (pdf/svg) plus raster ≥300 dpi. Size to
  journal columns (single ~89 mm, double ~183 mm). Keep fonts legible (mind the
  minimum size). Inherit a tuned publication theme.
