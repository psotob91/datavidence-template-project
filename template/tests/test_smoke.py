"""Smoke test — trivial, deterministic. Proves the pytest harness runs.

Run with:  pytest  (or `make test`)
Replace with real tests for the project's modules.
"""


def test_arithmetic_is_deterministic() -> None:
    assert 2 * 21 == 42


def test_toolchain_is_wired_up() -> None:
    assert True
