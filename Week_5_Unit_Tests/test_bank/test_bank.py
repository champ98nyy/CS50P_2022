# CS50P 2022 - PSET 5
# Back to the Bank -- Unit Tests

from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("hey") == 20
    assert value("Good Morning") == 100
    assert value("") == 100