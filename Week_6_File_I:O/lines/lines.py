# CS50P 2022 - PSET 6
# Lines of Code

"""
In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines.

If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py,
or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
"""

import sys

# Main function checks that 2 command-line arguments were provided and the 2nd argument is a .py file
# Function then attempts to open .py file, raising an exception error if the file does not exist.
# Otherwise, function reads file into memory, removes leading/trailing whitespace from all lines, then passes list of lines to line_count()
# line_count() returns the total qty of non-blank and non-commented-out lines of code in the file examined

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python  lines.py  filename.py")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Only Python files may be examined")

    else:
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                lines = f.readlines()
                lines = [line.strip() for line in lines] # Remove leading/trailing whitespace from every line

                line_count = lines_of_code(lines)

        except FileNotFoundError:
            sys.exit("File does not exist.")

    print(line_count)


# Custom function examines every list item (line of code) and increments the total lines of code counter only if
# the line is not blank and the line is not commented out. Finally, the total quantity is returned to main()

def lines_of_code(lines):
    line_count = 0

    for line in lines:
        if line.startswith("#"):
            pass

        elif line == "":
            pass

        else:
            line_count += 1

    return line_count

if __name__ == "__main__":
    main()