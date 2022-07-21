# CS50P 2022 - PSET 0
# Tip Calculator

"""
In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a
tip calculator for you, below! Well, we’ve written most of a tip calculator for you.

Unfortunately, we didn’t have time to implement two functions:
    - dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
    remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.

    - percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
    remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

Assume that the user will input values in the expected formats.
"""

# main function requests user inputs for price of meal and desired tip percentage, each converted/formatted using
# their respective functions (dollars_to_float, percent_to_float), then calculates the tip as the product of dollars and percent
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# dollars_to_float function takes a string parameter from user input, strips the "$" and casts the parameter to float,
# then returns the result

def dollars_to_float(d):
    return float(d.strip("$"))


# percent_to_float function takes string parameter from user input, strips the "%" and casts parameter to float,
# then returns the result of dividing by 100 (converts to percent)

def percent_to_float(p):
    p = float(p.strip("%"))
    return (p/100)

# Call main function
main()
