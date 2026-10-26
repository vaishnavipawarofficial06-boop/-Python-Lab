"""Tests for reusable Python Lab helpers."""

import pytest

from python_lab.math_tools import celsius_to_fahrenheit, is_even, second_largest


@pytest.mark.parametrize(
    ("celsius", "expected"),
    [(0, 32), (100, 212), (-40, -40)],
)
def test_celsius_to_fahrenheit(celsius: float, expected: float) -> None:
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.parametrize(("number", "expected"), [(2, True), (3, False), (0, True), (-4, True)])
def test_is_even(number: int, expected: bool) -> None:
    assert is_even(number) is expected


def test_second_largest_uses_distinct_values() -> None:
    assert second_largest([9, 1, 9, 4, 4]) == 4


@pytest.mark.parametrize("numbers", [[], [1], [5, 5]])
def test_second_largest_requires_two_distinct_values(numbers: list[int]) -> None:
    with pytest.raises(ValueError, match="two distinct"):
        second_largest(numbers)
