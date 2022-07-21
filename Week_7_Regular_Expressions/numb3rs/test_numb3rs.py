# CS50P 2022 - PSET 7
# NUMB3RS -- Unit Tests

from numb3rs import validate

# Test to ensure ip Address has exactly 4 numbers each separated by a period
def test_ip_format():
    assert validate(r'1') == False # Only 1 number
    assert validate(r'1.1') == False # Only 2 numbers
    assert validate(r'1.1.1') == False # Only 3 numbers
    assert validate(r'1.1.1.1') == True # Correct 4 numbers separted by periods
    assert validate(r'1.1.1.1.') == False # Correct 4 numbers, but with trailing period
    assert validate(r'1.1.1.1.1') == False # Too many numbers

# Test to ensure each number is between 0 - 255
def test_ip_numbers():
    assert validate(r'0.0.0.0') == True # Min Threshold
    assert validate(r'255.255.255.255') == True # Max Threshold
    assert validate(r'256.256.256.256') == False # Above Max Threshold
    assert validate(r'255.255.255.256') == False # All correct except last
    assert validate(r'001.010.1.001') == True # Leading zeros