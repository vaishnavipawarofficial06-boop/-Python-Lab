"""Intermediate practice: files, JSON, exceptions, OOP, and type hints.

These exercises use small in-memory examples so you can focus on Python
before introducing external services or databases.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """A product record with validated values."""

    name: str
    price: float
    quantity: int

    def total_value(self) -> float:
        """Return price multiplied by quantity."""
        # TODO: reject invalid values in __post_init__ and implement this.
        raise NotImplementedError


def safe_divide(numerator: float, denominator: float) -> float:
    """Divide two numbers; raise ValueError for a zero denominator."""
    # TODO: do not silently return zero for an invalid operation.
    raise NotImplementedError


def parse_positive_int(value: str) -> int:
    """Parse a strictly positive integer or raise ValueError."""
    # TODO: handle non-integer text and zero/negative values.
    raise NotImplementedError


def load_json_text(text: str) -> object:
    """Parse JSON text and raise a clear ValueError for invalid JSON."""
    # TODO: use the json standard library and chain the original exception.
    raise NotImplementedError


def median(values: list[float]) -> float:
    """Return the median; raise ValueError for an empty list."""
    # TODO: sort a copy, not the caller's list.
    raise NotImplementedError
