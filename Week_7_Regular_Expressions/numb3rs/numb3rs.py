# CS50P 2022 - PSET 7
# CS50 NUMB3RS

"""
In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which isn’t actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world,
typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range!
If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False,
respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries.
You’re welcome, but not required, to use re and/or sys.

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ...

...

if __name__ == "__main__":
    main()


Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions that collectively
test your implementation of validate thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_numb3rs.py

"""

import re

# Main function prompts user to input ip address, then validates the input and prints True/False based on results
def main():
    print(validate(input("IPv4 Address: ")))

# Custom function to validate ip address input by user
def validate(ip):

    # Match ip address format to regular expression. If not a match, return false. Otherwise split ip address into a list of just the numbers
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
        numbers = ip.split('.')

        # Check if each number is between 0 - 255. Return false if any are not, otherwise return true 
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True

    else:
        return False


if __name__ == "__main__":
    main()