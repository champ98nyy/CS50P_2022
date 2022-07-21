# CS50P 2022 - PSET 5
# Refueling

"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
    • convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage,
      an int between 0 and 100, inclusive. If X and/or Y is not an integer, then convert should raise a ValueError. If Y is 0, then convert
      should raise a ZeroDivisionError

    • gauge expects an int and returns a str that is:
        • "E" if that int is less than or equal to 1,
        • "F" if that int is greater than or equal to 99
        • and "Z%" otherwise, wherein Z is that same int
"""

# main function requests user input of a fraction, removes leading and trailing whitespace, then calls the convert() function and gauge() function to print the proper meter reading
# TypeError will cause the loop to start over again
def main():
    while True:
        fraction = input("Fraction: ").strip()

        try:
            percentage = convert(fraction)
            meter = gauge(percentage)
            print(meter)
            break

        except TypeError:
            continue


# Custom function takes user input of a fraction and returns the integer equivalent as a percentage
# If a ValueError or ZeroDivisionError occur, function returns nothing, resulting in main() function loop re-prompting user for input
def convert(fraction):
    top, bottom = fraction.split("/")

    try:
        gas = int(int(top)/int(bottom) * 100)
        # return gas

    except (ValueError, ZeroDivisionError):
        pass

    else:
        return gas


# Custom function takes integer percentage and returns the correct meter readout to main()
def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()