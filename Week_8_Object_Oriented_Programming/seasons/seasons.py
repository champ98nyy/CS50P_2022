# CS50P 2022 - PSET 8
# CS50 Seasons of Love

"""
Assuming there are 365 days in a year, there are 365 * 24 * 60 = 525,600 minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour).
But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them
could have additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since!
There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes with a datetime module that has a class called
date that can help, per docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes,
rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the
time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date,
per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:

from datetime import date


def main():
    ...


...


if __name__ == "__main__":
    main()

You’re welcome to import other (built-in) libraries. Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.

Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your implementation of any functions
besides main in seasons.py thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_seasons.py
"""

from datetime import date, timedelta
import inflect
import sys

# Main function requests user to input birthdate in YYY-MM-DD format, converts it to a datetime.date object assigned to birthdate variable
# Function then prints the length of time (in minutes written as words) user has been alive
# If user inputs invalid format for birthdate, program exits
def main():

    try:
        birthdate = date.fromisoformat(input("What is your Birthdate (YYYY-MM-DD)?: ").strip())
        print(f'{get_min_alive(birthdate)} minutes')

    except ValueError:
        sys.exit("Invalid Date Format")

# Custom fiunction takes user input birthdate and calculates the minutes they have been alive, first as an integer.
# Integer is then passed to min_in_words() function to be converted to words before returning that value to main()
def get_min_alive(birthdate):

    today = date.today()
    # print(f'INSIDE GET_MIN_ALIVE, BIRTHDATE IS: {birthdate}')
    time_alive = today - birthdate
    # print(f'TIME ALIVE: {time_alive}')
    days_alive = time_alive.days
    # print(f'DAYS ALIVE: {days_alive}')
    min_alive = days_alive * 24 * 60
    return min_in_words(min_alive)

# Custom function takes an integer value and converts it to words using inflect module
# Output is also formated to capitalize the first letter of the first word and to remove any occurences of the word, "and"
def min_in_words(min_alive):

    p = inflect.engine() # Initiate the class engine
    return p.number_to_words(min_alive, andword='').capitalize() # Convert int to words, capitalize letter of first word, remove "and" from string



if __name__ == "__main__":
    main()




# today = date.today()
# birthdate = date.fromisoformat('2021-07-07')
# since = today - birthdate


# days = since.days
# hours = days * 24
# minutes = hours * 60