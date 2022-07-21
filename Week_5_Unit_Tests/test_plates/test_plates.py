# CS50P 2022 - PSET 5
# Re-requesting a Vanity Plate -- Unit Tests

from plates import is_valid


# Input must contain 2 - 6 letters/numbers
def test_length():
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A") != True
    assert is_valid("AAAAAAA") != True


# User input in not case-sensitve
def test_capitalization():
    assert is_valid("aAaAaA") == True
    assert is_valid("aaaaaa") == True
    assert is_valid("aaAA11") == True


# If input includes numbers, they must be preceded by at least 2 letters and cannot be followed by any letters
def test_number_placement():
    assert is_valid("AA1234") == True
    assert is_valid("AAAAA1") == True
    assert is_valid("AAA123") == True
    assert is_valid("AA7AAA") != True
    assert is_valid("AAA22A") != True


# First 2 characters of input must be letters
def test_first_two():
    assert is_valid("12") != True
    assert is_valid("1A") != True
    assert is_valid("A1") != True


# If input includes "0" it cannot be the only number and must be preceded by a non-zero number
def test_zero_placement():
    assert is_valid("AA10") == True
    assert is_valid("AAA550") == True
    assert is_valid("AA1000") == True
    assert is_valid("AAAA01") != True
    assert is_valid("AA0234") != True


# Input cannot contain any punctuation
def test_punctuation():
    assert is_valid("ZYXWVU") == True
    assert is_valid("TEST11") == True
    assert is_valid("TEST1!") != True
    assert is_valid("TES.T3") != True