# CS50P 2022 - PSET 5
# Testing my twttr -- Unit Tests

from twttr import shorten

def test_shorten():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("abcdef") == "bcdf"
    assert shorten("") == ""
    assert shorten("aeiou") == ""
    assert shorten("1") == "1"
    assert shorten("sky fly why") == "sky fly why"
    assert shorten("HELLO, WORLD!") == "HLL, WRLD!"