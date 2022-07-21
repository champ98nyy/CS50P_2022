# CS50P 2022 - PSET 6
# Scourgify

"""
Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format.
Consider, for instance, this CSV file of students, before.csv, below:

name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
"Bones, Susan",Hufflepuff
"Boot, Terry",Ravenclaw
"Brown, Lavender",Gryffindor
...

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name),
escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter
to each student, as via mail merge, since it’d be strange to start a letter with:

Dear Potter, Harry,

Rather than with, for instance:

Dear Harry,

In a file called scourgify.py, implement a program that:

    • Expects the user to provide two command-line arguments:
        • the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
        • the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

    • Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import sys
import pandas as pd

# Main function checks that 2 command-line arguments were provided and the 2nd argument is a .csv file
# Function then attempts to open .csv file, raising an exception error if the file does not exist.
# Otherwise, function reads file into a pandas dataframe, then passes the df to tabulate(), printing the resulting menu

def main():
    """
    Main function checks that command-line arguments meet requirements, then cleans and re-formats data from source .csv file
    and saves result to a new .csv file
    """

    # Check that exactly 3 command-line arguments were provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python  scourgify.py  before.csv  after.csv")

    # Check that 2nd command-line argument is a .csv file
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Only .csv files may be used")

    # Begin
    else:
        try:
            df = pd.read_csv(sys.argv[1]) # Read .csv file into a pandas DataFrame

            # Create empty lists for students' first names, last names, and house names
            first_names = []
            last_names = []
            houses = []

            # Iterate through every record, separating into first name, last name then appending to the corresponding lists for each
            for x in df.name:
                full_name = x.split(",")
                last, first = full_name[0], full_name[1].strip()
                first_names.append(first)
                last_names.append(last)

            # Iterate through every record and add the house name to the houses list
            for y in df.house:
                houses.append(y)

            # Create a dictionary that includes all first names, last names, and houses
            data = {
                "first": first_names,
                "last": last_names,
                "house": houses
            }

            # Create a pandas DataFrame from the dictionary
            clean_df = pd.DataFrame(data)

            # Save cleaned-data DataFrame to a new .csv file
            clean_df.to_csv(sys.argv[2], index=False, mode='w', line_terminator='\r\n')

        # Check that file exists
        except FileNotFoundError:
            sys.exit("File does not exist.")

if __name__ == "__main__":
    main()