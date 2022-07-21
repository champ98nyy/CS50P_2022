# CS50P 2022 - PSET 3
# Fuel Guage

"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank. If, though, less than 1% remains, output E instead to indicate that the tank is empty. And if more than 99% remains, output F instead to indicate that the tank is full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

# main function will call the get_fraction function, evaluate the returned value and print the appropriate fuel guage display
def main():

    gas = get_fraction()

    print("E") if gas < 1 else print("F") if gas > 99 else print(f"{round(gas)}%")


# Custom function continues to prompt user to input a fraction, until input does not cause an Exception. Function then returns the product of the fraction and 100
def get_fraction():
    while True:
        try:
            top, bottom = input('Fraction: ').strip().split('/')
            final = int(top)/int(bottom)

            if final > 1:
                continue

        except (ValueError, ZeroDivisionError):
            continue

        return float(final * 100)


if __name__ == "__main__":
    main()