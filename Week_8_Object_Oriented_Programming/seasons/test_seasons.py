# CS50P 2022 - PSET 8
# Seasons of Love -- Unit Tests

import pytest
from seasons import get_min_alive, min_in_words

# Test to ensure first letter of first word is capitalized
def test_capital():
    assert min_in_words(1) == 'One'
    assert min_in_words(1) != 'one'
    assert min_in_words(1250) == 'One thousand, two hundred fifty'
    assert min_in_words(1250) != 'one Thousand, two hundred fifty'

# Test to ensure the word "and" is removed from output
def test_no_and():
    assert min_in_words(525600) == 'Five hundred twenty-five thousand, six hundred'
    assert min_in_words(525600) != 'Five hundred and twenty-five thousand, six hundred'