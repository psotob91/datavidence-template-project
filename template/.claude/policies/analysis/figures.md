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
- **Keep a vector master; raster is a derivative.** Always author and version-control a
  **vector master (SVG or PDF)** — the canonical, resolution-independent source for
  publication and graphic design. Export raster (**PNG/TIFF, never JPEG**) only as a
  derivative at the target resolution (**≥300 dpi; line art ≥600 dpi**). **EPS is legacy**
  — do not author new masters in it. Raster is unavoidable only for inherently pixel
  content (photographs / microscopy; heatmaps or scatter with millions of points) —
  rasterize that data layer while keeping axes and text vector. Size to journal columns
  (single ~89 mm, double ~183 mm); keep fonts legible; inherit a tuned publication theme.
