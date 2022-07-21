# CS50P 2022 - PSET 7
# Regular, um, Expressions -- Unit Tests

import pytest
from um import count


# Test to ensure occurences of "um" within a larger word (e.g. drum, alumni, yummy) do not get counted
def test_within_word():
    assert count('This food is, um, yummy.') == 1
    assert count('Carter plays the drums') == 0
    assert count('umm') == 0

# Test to ensure occurences of "um" are counted, regardless of what case they are in
def test_ignore_case():
    assert count('Um, why are you, um, here?') == 2
    assert count('He shouted, "UM, GO AWAY!", but she stayed.') == 1