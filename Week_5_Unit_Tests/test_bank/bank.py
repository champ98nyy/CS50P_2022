# CS50P 2022 - PSET 5
# Back to the Bank

"""
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns 0 if that str starts with “hello”,
20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively.
Only main should call print.
"""

# Main function requests user input of a greeting, removes leading/trailing spaces and assigns the value to the greeting variable
# The value() function is then called on greeting, and the outcome is assigned to the prize variable
# Finally, the value of prize is printed
def main():
    greeting = input("Greeting: ").strip()

    prize = value(greeting)

    print(prize)


# Custom function accepts greeting as a parameter, converts the string to all lowercase letters, then performs checks on the greeting to determine the value of the prize
def value(greeting):
    greeting = greeting.lower()

    try:
        # Check if "hello" is the first word in greeting string and return 0 if so
        if greeting[0:5] == "hello":
            return 0

        # Check if "h" is first character in greeting string and return 20 if so
        elif greeting[0] == "h":
            return 20

        # Otherwise, return "100"
        else:
            return 100

    # If user enters a blank input, and IndexError will occur. A blank input is the equivalent of no greeting, so return "100"
    except IndexError:
        return 100

if __name__ == "__main__":
    main()