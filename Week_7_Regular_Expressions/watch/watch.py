# CS50P 2022 - PSET 7
# CS50 Watch on YouTube

"""
In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value
of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL
will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain
no more than one such URL. If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0

Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries.
You’re welcome, but not required, to use re and/or sys.
"""

import re


# Main function passes HTML input by user prompt to parse() function, and prints shortened YouTube URL if input meets requirements
def main():
    print(parse(input("HTML: ")))


# Custom function checks HTML input by user to ensure it contains an iframe element with a youtube URL
# If so, function returns a shortened URL version of youtube URL
def parse(s):

    # Check HTML input for iFrame RegEx
    if re.search(r'^<iframe\s.+><\/iframe>$', s, re.IGNORECASE):

        # Check iFrame for YouTube URL RegEx
        yt_url = re.search(r'(https?):\/\/(www\.)?youtube\.com\/embed\/([a-z0-9_]+)', s, re.IGNORECASE)

        # If iFrame and YT URL pass tests, return concatenation of the below URL beginning and the last
        if yt_url:
            return 'https://youtu.be/' + yt_url.groups()[-1]


if __name__ == "__main__":
    main()