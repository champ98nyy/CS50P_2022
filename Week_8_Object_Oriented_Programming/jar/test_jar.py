# CS50P 2022 - PSET 8
# Cookie Jar -- Unit Tests

import pytest
from jar import Jar

# Test to ensure a new jar object is initialized with a capacity of 12 and a size of 0
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

# Test to ensure the string representation of a jar object displays the cookie emoji as many times as there are cookies in the jar
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

# Test to ensure the deposit() adds n cookies to the jar
def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.deposit(1)
    assert jar.size == 9
    jar.deposit(3)
    assert jar.size == 12

# Test to ensure the withdraw() removes n cookies from the jar
def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0

# Test to ensure a ValueError gets raised if a jar is over capacity
def test_ValueError_over():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(13)

# Test to ensure a ValueError gets raised if a jar is under 0
def test_ValueError_under():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(1)