# CS50P 2022 - PSET 4
# Adieu, Adieu

"""
In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:
    • Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:
    • Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one "and", three names with two "commas" and one "and", and n names with n-1 "commas" and one "and", as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""



# Initialize an empty list called names. This will store all items input by user

names = []

# Continue prompting user to enter names until they press CTRL-d on their keyboard to finalize inputs.
# Each time a name is input, append it to the names list
while True:
    try:
        name = input().strip()
        names.append(name)

    except EOFError:
        break

# Count the number of names entered and assign the value to the qty variable
qty = len(names)

# If the user only entered one name, print the line from the song using their name at the end
if qty == 1:
    print(f"Adieu, adieu, to {names[0]}")

# If the user entered exactly 2 names, print the line from the song using the first name entered, followed by "and" followed by the second name entered
elif qty == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")

# If the user entered more than 2 names, print the line from the song using a comma-separated list of all names except for the final name, followed by "and" followed by the final name entered
elif qty > 2:
    names_a = names[0:(qty - 1)] # names_a will create a slice of the names list, including all names except the final name entered

    names_a = ", ".join(names_a) # the .join() method will be called turning the list slice into a comma-separated string

    print(f"Adieu, adieu, to {names_a}, and {names[-1]}")