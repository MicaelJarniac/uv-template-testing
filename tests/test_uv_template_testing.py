"""Testing for uv-template-testing."""

import pytest
from hypothesis import given
from hypothesis import strategies as st
from inline_snapshot import snapshot
from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore[import]

from uv_template_testing import make_greeting


def test_make_greeting_benchmark(benchmark: BenchmarkFixture) -> None:
    """Test `make_greeting`."""
    result = benchmark(make_greeting, "Micael Jarniac")
    assert result == "Hello, Micael Jarniac. Welcome to your new project!"


@given(name=st.text())
def test_make_greeting_hypothesis(name: str) -> None:
    """Test `make_greeting`."""
    result = make_greeting(name)
    assert result == f"Hello, {name}. Welcome to your new project!"


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Foo", snapshot("Hello, Foo. Welcome to your new project!")),
        ("Bar", snapshot("Hello, Bar. Welcome to your new project!")),
    ],
)
def test_make_greeting_snapshot(name: str, expected: str) -> None:
    """Test `make_greeting`."""
    result = make_greeting(name)
    assert result == expected
