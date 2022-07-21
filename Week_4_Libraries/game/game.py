# CS50P 2022 - PSET 4
# Guessing Game

"""
I’m thinking of a number between 1 and 100…

What is it?
It’s 50! But what if it were more random?

In a file called game.py, implement a program that:

    • Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
    • Randomly generates an integer between 1 and n, inclusive.
    • Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        • If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        • If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        • If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random

# Main function first calls the get_level() function to get user input of an upper threshold level.
def main():
    level = get_level()

    # Once the user has entered a valid level, generate a random integer between 1 - the level. Assign this value to the answer variable.
    # This will be the number the user then attemps to guess in order to win the game.
    answer = random.randint(1, level)

    # main() function then calls get_guess(answer) function, passing the correct answer as a parameter
    get_guess(answer)

# Custom function that will continue requesting the user to input a guess at the answer, and provide feedback to let them know if they are too high or too low with their guess.
# If guess is not a positive integer, user will be re-prompted without a hint about their previous guess
# Once user guesses correctly, they are informed and the program ends
def get_guess(answer):
    while True:
        try:
            guess = int(input("Guess: ").strip())

            if guess < answer:
                print("Too small!")
                continue

            elif guess > answer:
                print("Too large!")
                continue

            else:
                print("Just right!")
                break

        except ValueError:
            continue

# Custom function that will continue requesting the user to input a level number until they input a positive integer
# Function then returns the level to the main function, which is used as a parameter when randomly generating the correct answer the user will need to guess
def get_level():
    while True:
        try:
            level = int(input('Level: ').strip())

            if level <= 0:
                continue

        except ValueError:
            continue

        return level

if __name__ == "__main__":
    main()























# import random

# def main():
#     level = get_level()
#     print("LEVEL: ", level)

    # Once the user has entered a valid level, generate a random integer between 1 - the level. Assign this value to the answer variable.
    # This will be the number the user then attemps to guess in order to win the game.
    # answer = random.randint(1, level)
    # print("ANSWER: ", answer)

    # user_guess = get_guess(answer)

    # if get_guess(answer)
    #         guess = get_guess(answer)

    #         if guess < answer:
    #             print("Too small!")
    #             continue

    #         elif guess > answer:
    #             print("Too large!")
    #             continue

    #         else:
    #             print("Just right!")
    #             break

    #     except ValueError:
    #         continue


# def get_level():
#     while True:
#         try:
#             level = int(input('Level: ').strip())

#             if level <= 0:
#                 continue

#         except ValueError:
#             continue

#         return level

# # def get_guess(answer):
# #     guess = int("Guess: ").strip()

# #     return guess

# def get_guess(answer):
#     while True:
#         try:
#             guess = int("Guess: ").strip()

#             if guess < answer:
#                 print("Too small!")
#                 continue

#             elif guess > answer:
#                 print("Too large!")
#                 continue

#             else:
#                 print("Just right!")

#         except ValueError:
#             continue

# if __name__ == "__main__":
#     main()