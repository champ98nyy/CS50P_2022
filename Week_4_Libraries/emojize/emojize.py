# CS50P 2022 - PSET 4
# Emojize

"""
Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍.
Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
"""

import emoji

# Main function prompts user to input text, then calls to_emoji() function to convert string into "emojized" version, then prints "emojized" version of original user input
def main():
    print(to_emoji(input("Input: ").strip()))

# Custom function takes string as a parameter, then returns "emojized" version of string, accounting for both Emoji codes defined by the unicode consortium, as well as multiple aliase codes.
def to_emoji(text):
    return emoji.emojize(text, language='alias')

if __name__ == "__main__":
    main()
