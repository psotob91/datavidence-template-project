# _targets.R — {targets} pipeline definition.
# Run with:  targets::tar_make()        (or `make pipeline`)
# Inspect:   targets::tar_read(<name>)   /  targets::tar_visnetwork()
# Docs:      https://books.ropensci.org/targets/

library(targets)

# Global options for every target in this pipeline.
tar_option_set(
  packages = character(0)  # TODO: list packages your targets need, e.g. c("dplyr")
)

# TODO: move reusable functions into R/ and source them here, e.g.
#   tar_source()  # sources every .R file under R/

# The pipeline is the final expression: a list() of tar_target() objects.
# Below is a trivial, deterministic, runnable example — replace it.
list(
  # A raw input. Deterministic seed value so `tar_make()` is reproducible.
  tar_target(
    name = raw_value,
    command = 42L
  ),
  # A derived target that depends on `raw_value`.
  tar_target(
    name = doubled,
    command = raw_value * 2L
  )
  # TODO: add real targets: data import, cleaning, modeling, reporting.
  # TODO: add a tarchetypes::tar_quarto() target to render analysis/report.qmd.
)
