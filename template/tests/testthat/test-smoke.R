# Smoke test — trivial, deterministic. Proves the test harness runs.
# Run with:  testthat::test_dir("tests/testthat")  (or `make test`)
# Replace with real tests for the functions in R/.

test_that("arithmetic is deterministic", {
  expect_equal(2L * 21L, 42L)
})

test_that("the test toolchain is wired up", {
  expect_true(TRUE)
})
