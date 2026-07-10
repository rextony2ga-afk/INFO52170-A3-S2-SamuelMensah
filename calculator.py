# calculator.py - Created by Samuel Mensah
# calculator.py


def add(number1, number2):
    """Add two numbers and return the result."""
    return number1 + number2


def subtract(number1, number2):
    """Subtract the second number from the first."""
    return number1 - number2

    # test_calculator.py

from calculator import add, subtract


def test_add():
    """This test should pass."""
    assert add(2, 3) == 5


def test_subtract():
    """This test intentionally fails for the CI demonstration."""
    assert subtract(10, 4) == 5

    subtract(10, 4)

    E       assert 6 == 5
E        +  where 6 = subtract(10, 4)

FAILED test_calculator.py::test_subtract
