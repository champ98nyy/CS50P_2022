# CS50P 2022 - PSET 2
# Just setting up my twttr

"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""

# Create a list of vowels to use for checking if each letter in the tweet is a vowel
vowels = ["a", "e", "i", "o", "u"]

# Request user input of a Tweet, remove leading/trailing spaces and assign value to tweet variable
tweet = input("Input: ").strip()

# Split the tweet into a list of words and assign value to words variable
words = tweet.split()

# Create an empty list called final
# Loop through each word in the list of words and create a list of characters for each word, assigning the value to the letters variable
final = []
for word in words:
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
    print(final_word)

# Once all vowel-less words are added to the list, use the join method with a space to create the final string output of the tweet
final_tweet = ' '.join(final)
print("FINAL TWEET: ", final_tweet)