# CS50P 2022 - PSET 5
# Refueling -- Unit Tests
import pytest
from fuel import convert, gauge


# Test to confirm convert() function takes a string of a fraction as a parameter and returns the int equivalent as a percentage
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("0/1") == 0


# Test to confirm gauge() function takes an int as a parameter returns the correct corresponding string
def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"


# Test to confirm convert() function raises a ZeroDivisionError if denominator of fraction is a 0
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("7/0")


# Test to confirm convert() function raises a ValueError if non numeric characters are input as either the numerator or denominator of the fraction
def test_value_error():
    with pytest.raises(ValueError):
        convert("hello/world")
        convert("1/two")