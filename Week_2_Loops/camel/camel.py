# CS50P 2022 - PSET 2
# camelCase

"""
In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words,
whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable
for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first
name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance,
those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
"""

# Request user input, remove leading/trailing spaces, then assign to camel_case variable
camel_case = input("camelCase: ").strip()

# Create a list of all letters from the input string
letters = list(camel_case)

# Loop over every character in the list of letters and check whether it is a capital letter
# If a character is uppercase, convert the letter to lowercase, concatenate an underscore ("_") before the letter and assign the new string to the lowercase variable
# Using list comprehension, loop through all characters again, this time replacing the capital letter with the new underscored lowercase letter
for letter in letters:
    if letter.isupper() == True:
        lower = "_" + letter.lower()
        letters = [lower if y==letter else y for y in letters]

# Once all uppercase letters have been converted in previous step, rejoin all the letters in the list to form a single string and assign the value to the snake_case variable
snake_case = 'Z'.join(letters)
print("SNAKE CASE: ", snake_case)