# CS50P 2022 - PSET 7
# CS50 Response Validation

"""
When creating a Google Form that prompts users for a short answer (or paragraph), it’s possible to enable response validation and require that the user’s
input match a regular expression. For instance, you could require that a user input an email address with a regex like this one:

^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

Or you could more easily use Google’s built-in support for validating an email address, per the screenshot below, much like you could use a library in your own code.

In a file called response.py, using either validator-collection or validators from PyPI, implement a program that prompts the user for an email address
via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address. You may not use re. And do not validate whether
the email address’s domain name actually exists.
"""


from validator_collection import checkers

# Main function evaluates validity of user input email address and prints outcome
def main():
    print('Valid') if checkers.is_email(input("Email: ").strip()) else print('Invalid')

if __name__ == "__main__":
    main()