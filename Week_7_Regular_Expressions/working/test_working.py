# CS50P 2022 - PSET 7
# Working 9 to 5 -- Unit Tests

import pytest
from working import convert

# Test to ensure PM times are the result of adding 12 to the original input time
def test_add12():
    assert convert('3:00 PM to 11:00 PM') == '15:00 to 23:00'
    assert convert('3:00 AM to 11:00 AM') == '03:00 to 11:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') != '09:00 to 05:00'

# Test to ensure a leading 0 gets added to any time with a 1-digit hour in the output (i.e. 9:00 should be formatted as 09:00)
def test_leading0():
    assert convert('8:00 AM to 4:00 PM') == '08:00 to 16:00'
    assert convert('8:00 AM to 4:00 PM') != '8:00 to 16:00'
    assert convert('1 AM to 9 AM') == '01:00 to 09:00'

# Test to ensure times between 12:00 AM - 12:59 AM are formatted in the output with '00' for the hour
def test_12AM_hour():
    assert convert('12 AM to 9 AM') == '00:00 to 09:00'
    assert convert('12 AM to 9 AM') != '12:00 to 09:00'
    assert convert('12:15 AM to 12:55 AM') == '00:15 to 00:55'
    assert convert('3:00 PM to 12:00 AM') == '15:00 to 00:00'

# Test to ensure a ValueError gets raised if a user omits "to" in their working hours input
def test_ValueError_to():
    with pytest.raises(ValueError):
        convert('9:00 AM 5:00 PM')