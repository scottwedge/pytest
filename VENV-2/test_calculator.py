import pytest 

from calculator import Calculator, CalculatorError, CalculatorZeroDivError

def test_add():
    calc = Calculator()      # Arrange

    result = calc.add(3, 5)  # Act

    assert result == 8       # Assert


def test_add_weird_stuff():
    calc = Calculator()      # Arrange

    with pytest.raises(CalculatorError):
        result = calc.add("three", 5)  # Act


def test_add_weirder_stuff():
    calc = Calculator()      # Arrange

    with pytest.raises(ZeroDivisionError):
        result = calc.add(1/0, 5)  # Act


def test_subtract():
    calc = Calculator()      # Arrange

    result = calc.subtract(9, 5)  # Act

    assert result == 4       # Assert


def test_multiply():
    calc = Calculator()      # Arrange

    result = calc.multiply(3, 5)  # Act

    assert result == 15      # Assert


def test_divide():
    calc = Calculator()      # Arrange

    result = calc.divide(8, 2)  # Act

    assert result == 4       # Assert

