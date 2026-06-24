# .Rprofile — activates the renv project library on R startup.
# Guarded so the project still loads on a fresh checkout (before `make setup`
# has generated renv/activate.R and the lockfile).
if (file.exists("renv/activate.R")) {
  source("renv/activate.R")
}
