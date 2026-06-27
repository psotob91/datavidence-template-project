# _targets.R — {targets} pipeline definition (the reproducible spine).
# Run:      targets::tar_make()          (or `make test` / `make all`)
# Inspect:  targets::tar_read(<name>)    /  targets::tar_visnetwork()
# Reset:    `make reset`  (tar_destroy + clean data/derived) then `make all` to rebuild from zero
# Docs:     https://books.ropensci.org/targets/
#
# Governance: heavy computation lives HERE and in R/ (see .claude/policies/analysis/).
# The Quarto notebooks under analysis/ narrate & report — they do NOT do ETL.

library(targets)
library(tarchetypes)  # tar_quarto()

# Reproducibility: {targets} derives a deterministic per-target seed from this
# global seed — do not rely on a single top-level set.seed().
# See .claude/policies/analysis/reproducibility.md
tar_option_set(
  # Recommended "born-in" stack — install ON DEMAND via renv, only what you use
  # (see .claude/policies/analysis/regenerables.md & data-onboarding.md):
  #   wrangling: data.table (+ collapse)     IO    : rio, arrow, haven
  #   dates    : clock                        paths : here
  #   validate : pointblank                   miss  : mice
  #   tables   : gtsummary (+ gt, flextable)  figs  : ggplot2 (+ ggsci, patchwork)
  #   models   : survival, broom, emmeans, marginaleffects, performance, tidycmprsk
  #   big data : duckdb, duckplyr             repro : withr, sessioninfo, labelled
  packages = character(0),  # e.g. c("data.table", "gtsummary")
  seed = 1L
)

# Reusable functions live in R/ — extracted ONLY when scaling, under the gate in
# .claude/policies/analysis/incremental-functions.md. Source them all:
tar_source()  # sources every .R file under R/

# The pipeline mirrors the ordered notebooks: ingest -> IDA -> clean -> model ->
# report. 05_report.qmd is rendered by tar_quarto so its inline numbers come
# straight from the targets below (see results-writing.md).
list(
  # --- example targets (replace with real ones) -------------------------------
  tar_target(name = raw_value, command = 42L),
  tar_target(name = doubled,   command = raw_value * 2L),

  # --- render the narrative report (reads targets via tar_read) ---------------
  tar_quarto(name = report, path = "analysis/05_report.qmd")

  # TODO: real targets — onboard (data/raw) -> validate (contracts/) ->
  # clean (data/derived) -> model (R/) -> report. Keep ETL out of the .qmd.
)
