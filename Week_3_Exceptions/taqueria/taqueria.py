# CS50P 2022 - PSET 3
# Felipe's Taqueria

"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank. If, though, less than 1% remains, output E instead to indicate that the tank is empty. And if more than 99% remains, output F instead to indicate that the tank is full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

# Create a menu dict containing all items (keys) and their corresponding prices (values)
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Declare a total variable and set the value equal to zero
total = float(0)

# Run a while loop that continues to ask user to input a menu item until they press CTRL-d on their keyboard to end the order
# In each iteration of the loop, prompt user to input item name, assign value of corresponding price, add price to total and then inform user of current total
# If user inputs an incorrect item name, re-prompt user for another item

while True:
    try:
        item = input("Item: ").strip().title()
        price = float(menu[item])
        total += price
        print("Total: ${:.2f}".format(total))

    except KeyError:
        continue

    # User pressed CTRL-d on keyboard to end order -- first add a linebreak so terminal cursor goes to next line before program ends
    except EOFError:
        print("\n")
        break