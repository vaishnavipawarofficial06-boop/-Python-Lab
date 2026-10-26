"""Small, validated math helpers used by the Python Lab exercises."""

from __future__ import annotations


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def is_even(number: int) -> bool:
    """Return whether an integer is divisible by two."""
    return number % 2 == 0


def second_largest(numbers: list[int]) -> int:
    """Return the second-largest distinct integer.

    Raises:
        ValueError: If fewer than two distinct values are provided.
    """
    distinct = sorted(set(numbers))
    if len(distinct) < 2:
        raise ValueError("at least two distinct numbers are required")
    return distinct[-2]
