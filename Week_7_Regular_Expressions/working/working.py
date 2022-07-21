# CS50P 2022 - PSET 7
# CS50 Working 9 to 5

"""
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the
corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there
will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

    • 9:00 AM to 5:00 PM
    • 9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But
do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any
other libraries. You’re welcome, but not required, to use re and/or sys.


import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()


Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions
that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py
"""

import re

# Main function passes 12-Hour Clock formatted working hours input by user prompt to convert() function, and prints 24-Hour Clock conversion
def main():
    print(convert(input("Hours: ")))

# Custom function checks working hours input by user to ensure both times are formatted in proper 12-Hour Clock format and input fully matches RegEx
# If so, function returns a 24-Hour Clock formatted conversion of original user input
def convert(s):

    # Check working hours input against RegEx
    matches = re.search(r'^(?P<hour1>([1-9]{1}|[1]{1}[0-2]{1})):?(?P<min1>([0-5]{1}[0-9]{1}))?\s(?P<am_pm1>([AP]M))\sto\s(?P<hour2>([1-9]{1}|[1]{1}[0-2]{1})):?(?P<min2>([0-5]{1}[0-9]{1}))?\s(?P<am_pm2>([AP]M))$', s)

    # If working hours matches RegEx format, create a dict of the pre-definied capture groups, then set assign each value to corresponding variable names
    if matches:
        time_parts = matches.groupdict()

        hour1 = time_parts['hour1']
        hour2 = time_parts['hour2']
        min1 = time_parts['min1']
        min2 = time_parts['min2']
        am_pm1 = time_parts['am_pm1']
        am_pm2 = time_parts['am_pm2']

        # Check if either time is PM. If so, add 12 to the time to get 24-hour clock format
        hour1 = str(int(hour1) + 12) if am_pm1 == 'PM' and int(hour1) != 12 else hour1
        hour2 = str(int(hour2) + 12) if am_pm2 == 'PM' and int(hour2) != 12 else hour2

        # Check if either time is in the 12AM hour. If so, set the hour equal to 00
        hour1 = '00' if hour1 == '12' and am_pm1 == 'AM' else hour1
        hour2 = '00' if hour2 == '12' and am_pm2 == 'AM' else hour2

        # Check if either hour is between 1 - 9. If so, add a leading 0 to the hour
        hour1 = hour1.zfill(2) if 1 <= int(hour1) <= 9 else hour1
        hour2 = hour2.zfill(2) if 1 <= int(hour2) <= 9 else hour2

        # Check if either time included minutes along with the hours. If not, add :00 to hour to create final time
        time1 = f'{hour1}:{min1}' if min1 else f'{hour1}:00'
        time2 = f'{hour2}:{min2}' if min2 else f'{hour2}:00'

        # Return final string to main()
        return f'{time1} to {time2}'

    # Raise a ValueError if user input does not match RegEx
    else:
        raise ValueError


if __name__ == "__main__":
    main()