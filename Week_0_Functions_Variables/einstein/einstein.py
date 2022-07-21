# CS50P 2022 - PSET 0
# Einstein

"""
Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc2,
wherein E represents energy (measured in Joules), m represents mass (measured in kilograms), and
c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al.
Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""

# Main function takes user input then prints the result of passing response through convert function
def main():
    mass = input("What is the mass of the object? ")
    print("Energy: ", convert(mass), "Joules")

# Convert function takes integer literal, float literal, or string literal parameter from user input, casts parameter to integer,
# then returns a formatted result of the E=mc2 equation
def convert(mass):
    energy = int(mass) * (300000000**2)
    return "{:,}".format(energy)

main()