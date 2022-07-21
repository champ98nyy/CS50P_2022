# CS50P 2022 - PSET 5
# Testing my twttr

"""
In a file called twttr.py, reimplement Setting up my twttr
from Problem Set 2, restructuring your code per the below,
wherein shorten expects a str as input and returns that same
str but with all vowels (A, E, I, O, and U) omitted, whether
inputted in uppercase or lowercase.

Then, in a file called test_twttr.py, implement one or
more functions that collectively test your implementation
of shorten thoroughly, each of whose names should begin with test_
so that you can execute your tests with:
pytest test_twttr.py
"""

# Main function requests user input of a Tweet, removes leading/trailing spaces, calls the shorten() function on the string and assigns the return value to the tweet variable
# Function then prints final shortened Tweet
def main():
    tweet = shorten(input("Input: ").strip())

    print(tweet)


# Custom function takes a string from original tweet input by user as a parameter, splits the string into a list of words, removes all vowels, converts the list of words back to a single string and returns the string to the main() function
def shorten(tweet):
    # Create a list of vowels to use for checking if each letter in the tweet is a vowel
    vowels = ["a", "e", "i", "o", "u"]

    # split string into list of words
    tweet = tweet.split()

    # Create an empty list called final
    # Loop through each word in the list of words and create a list of characters for each word, assigning the value to the letters variable
    final = []
    for word in tweet:
        letters = list(word)

        # Create an empty list called new_letters
        # Start a nested loop iterating over each letter in the list of letters for the current word in the list of words
        new_letters = []
        for letter in letters:

            # If the current letter is a vowel, set the temp_letter variable equal to an empty string, otherwise set the temp_letter variable equal to the current letter
            if letter.lower() in vowels:
                temp_letter = ""
            else:
                temp_letter = letter

            # Add the temp_letter to the list of new_letters (if it was a vowel, it will add an empty string which will be eliminated in next step)
            new_letters.append(temp_letter)

        # After checking all letters in the word, use the join method on the list of new_letters to create the final word (without any vowels)
        final_word = ''.join(new_letters)

        # Add the final word to the final list
        final.append(final_word)

    # Once all vowel-less words are added to the list, use the join method with a space to create the final string output of the shortened tweet
    shortened_tweet = ' '.join(final)

    return shortened_tweet


if __name__ == "__main__":
    main()