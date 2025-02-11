"""Testing for uv-template-testing."""

from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore[import]

from uv_template_testing import make_greeting


def test_make_greeting(benchmark: BenchmarkFixture) -> None:
    """Test `make_greeting`."""
    result = benchmark(make_greeting, "Micael Jarniac")
    assert result == "Hello, Micael Jarniac. Welcome to your new project!"
