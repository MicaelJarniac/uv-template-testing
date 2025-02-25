"""Benchmarking for uv-template-testing."""

from uv_template_testing import make_greeting


class TimeSuite:
    """A benchmark suite for timing uv-template-testing."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `name` attribute."""
        self.name = "Micael Jarniac"

    def time_make_greeting(self) -> None:
        """Benchmark the `make_greeting` function for its execution time."""
        make_greeting(self.name)


class MemSuite:
    """A benchmark suite for measuring the memory usage of uv-template-testing."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `name` attribute."""
        self.name = "Micael Jarniac"

    def mem_make_greeting(self) -> str:
        """Benchmark the `make_greeting` function for its memory usage."""
        return make_greeting(self.name)
