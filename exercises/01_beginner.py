"""Beginner practice: variables, input, conditions, loops, and basic math.

Run with: python exercises/01_beginner.py
Complete the TODOs, then run the file.
"""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    # TODO: strip whitespace and return a greeting using the cleaned name.
    raise NotImplementedError


def is_even(number: int) -> bool:
    """Return True when number is even."""
    # TODO: implement without converting the number to a string.
    raise NotImplementedError


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    # TODO: F = C * 9 / 5 + 32
    raise NotImplementedError


def fizz_buzz(limit: int) -> list[str]:
    """Return FizzBuzz values from 1 through limit inclusive.

    Multiples of 3 become 'Fizz', multiples of 5 become 'Buzz',
    and multiples of both become 'FizzBuzz'.
    """
    # TODO: validate limit and implement the loop.
    raise NotImplementedError


def main() -> None:
    """Small runnable demonstration once exercises are implemented."""
    print("Welcome to Python Lab!")
    print("Complete the TODOs in this file to unlock the demonstrations.")


if __name__ == "__main__":
    main()
