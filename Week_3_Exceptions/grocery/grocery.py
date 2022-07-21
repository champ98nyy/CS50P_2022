# CS50P 2022 - PSET 3
# Grocery List

"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
"""

# Initialize an empty list called grocery_list. This will store all items input by user

grocery_list = []

# Continue prompting user to enter a grocery list item until they press CTRL-d on their keyboard to finalize inputs.
# Each time an item is input, append it to the grocery_list list
while True:
    try:
        item = input().strip()
        grocery_list.append(item)

    except EOFError:
        break

# Sort the grocery_list, alphabetically
grocery_list.sort()

# Initialize an empty dict to store each grocery item added to the list (keys) along with how many times each item was added (values)
totals = {}

# Loop through grocery_list. In each iteration, check if the item is already a key in the totals dictionary. If it is, increase the corresponding quantity by 1 and update the dictionary
# Otherwise, add the item to the dictionary and set the quantity to 1
for item in grocery_list:

    if item in totals.keys():
        qty += 1
        totals.update({item: qty})

    else:
        qty = 1
        totals.update({item: qty})

# For each key/value pair in the dictionary, print the value then the key (in all caps) separated by a space
for item in totals:
    print(f"{totals[item]} {item.upper()}")