# CS50P 2022 - PSET 1
# Deep

"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

# Request user input, remove leading/trailing spaces, convert string to all lowercase, then assign to greeting answer
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# Output "Yes" if response is either "42", "forty-two" or "forty two" otherwise output "No"
print("Yes") if answer == "42" or answer == "forty-two" or answer == "forty two" else print("No")


# if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
#     print("Yes")
# else:
#     print("No")