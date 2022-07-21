# CS50P 2022 - PSET 0
# Making Faces

"""
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face.
Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input
with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as
a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input,
and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own
as an argument to input. Be sure to call main at the bottom of your file.
"""



# Main function takes user input then prints the result of passing response through convert function
def main():
    x = input("Which emoticons would you like converted to emojis? ")
    print(convert(x))

# Convert function takes string parameter, replaces emoticon "slightly smiling face" and "slightly frowning face"
# with emoji equivalents: "🙂" and "🙁"
def convert(x):
    y = x.replace(":)", "🙂").replace(":(", "🙁")
    return y

# Call main function
main()

