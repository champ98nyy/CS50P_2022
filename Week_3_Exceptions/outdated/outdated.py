# CS50P 2022 - PSET 3
# Outdated

"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design.
Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically
in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country,
formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month
in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days.
"""

# Main function prompts user to enter a date, checks that input matches 1 of 2 valid formats, and if so, prints the date in YYYY-MM-DD format. Otherwise, user will be re-prompted to enter a valid date
def main():
    while True:
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        input_date = input("Date: ").strip()

        # Initial check to rule out case where user enters name of month, then uses slashes to separate month, day, year (re-prompt if so)
        if input_date[0].isalpha() and "/" in input_date:
            input_date = input("Date: ").strip()

        # Convert input date into list of strings, removing any commas and slashes
        input_date = input_date.replace(',', '').replace('/', ' ').split()

        # Assign values (by index) to month, day and year variables
        month, day, year = input_date[0], input_date[1], input_date[2]

        # Call custom functions to check validity of month, day and year from user's input. Re-prompt user for date if any functions return False
        if valid_month(month, months) == True and valid_day(day) == True and valid_year(year) == True:
            break

    # Once month, day and year are all valid, enumerate over the list of months, initializing a dictionary that pairs each month with its corresponding number. Start from 1 to counteract 0-index property
    # Looking at each key/value pair in the dictionary, determine if current value of month variable is the name of a month, or its corresponding number. If the latter, re-assign the month variable to equal the corresponding number
    # Otherwise, the user must have entered a number for the month, so variable can remain as is until next step
    months = dict(enumerate(months, 1))
    for key, value in months.items():
        if month == value:
            month = key
        else:
            pass

    # Using string.zfill() method, format month and day to have 2 digits with leading zeros, if needed
    month = str(month).zfill(2)
    day = str(day).zfill(2)

    # With all variables now correctly formated as individual strings, combine into a list in desired year, month, day order.
    # Then join the elements of the list into a single string, separated by dashes and print the final date
    final_date = [year, month, day]
    final_date = "-".join(final_date)

    print(final_date)

# Custom function to determine validity of month input by user
# First checks if a title-cased version of the month is in the pre-defined list of months (this would mean user input the valid name of a month, rather than the number or any other string that is not a month's name)
# The input is valid and function can return True
def valid_month(month, months):
    if month.title() in months:
        return True

    # If the month input does not pass the initial test above, try casting the month as an integer and checking if it's value is between 1 - 12 (valid numbers for months).
    # If a ValueError is thrown, it means the user entered an invalid name for a month, since non-numeric characters cannot be cast as an integer. Function will return False and user will be re-prompted to enter a date
    # If no ValueError occurs, but value is not between 1 - 12, function will return False and user will be re-prompted to enter a date
    # If yes, the month is valid and function can return True.
    try:
        if int(month) in range(1, 13):
            return True

    except ValueError:
        return False

# Custom function to determine validity of day input by user
# Function will first attempt to cast the value of day as an integer. If a ValueError is thrown, user did not enter numeric characters for the day. Function will return False and re-prompt user to enter a date
def valid_day(day):
    try:
        day = int(day)

    except ValueError:
        return False

    # If the value of day was entered as numeric characters, check that the value falls within the range of 1 - 31 (min/max qty of days in a month)
    # If yes, function will return True. Otherwise, it will return False and user will be re-prompted to enter a date
    if int(day) in range(1, 31):
        return True

# Custom function to determine validity of year input by user
# Function casts year value as an integer and checks that it falls within the range of 1000 - 9999 (covers all years that meet required 4-digit year format)
# Returns True if so, otherwise returns False and user is re-prompted to enter a date
def valid_year(year):
    if int(year) in range (1000, 10000):
        return True

if __name__ == "__main__":
    main()