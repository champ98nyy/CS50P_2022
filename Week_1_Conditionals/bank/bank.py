# CS50P 2022 - PSET 1
# Home Federal Savings Bank

"""
In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.”
Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes
a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h”, output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively.
"""

# Request user input, remove leading/trailing spaces, convert string to all lowercase, then assign to greeting variable
greeting = input("Greeting: ").strip().lower()

# Check if "hello" is the first word in response string and output $0 if so
if greeting[0:5] == "hello":
    print("$0")

# Check if "h" is first character in response and output $20 if so
elif greeting[0] == "h":
    print("$20")

# Otherwise, output "$100"
else:
    print("$100")