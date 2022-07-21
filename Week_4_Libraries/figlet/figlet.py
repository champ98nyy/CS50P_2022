# CS50P 2022 - PSET 4
# Figlet

"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art.

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:
    •Expects zero or two command-line arguments:
        • Zero if the user would like to output text in a random font.
        • Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.

    •Prompts the user for a str of text.
    •Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys
from pyfiglet import Figlet

# Main function first calls the which_font() function to determine if command-line arguments are valid and if so, determine which Figlet font to use when printing
# If command-line arguments are valid, function requests user input, strips off leading/trailing spaces and then prints input using Figlet font
def main():
    f = which_font()
    print(f.renderText(input("Input: ").strip()))

# Custom function checks command-line arguments then returns a Figlet font if arguments are valid, otherwise exits the program and informs user of Invalid Usage of command-line arguments
def which_font():
    if len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in ["slant", "rectangles", "alphabet"]:
            f = Figlet(font=sys.argv[2])
            return f
        else:
            sys.exit("Invalid usage")

    elif len(sys.argv) == 1:
        f = Figlet()
        return f

    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()