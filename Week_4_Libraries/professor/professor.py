# CS50P 2022 - PSET 4
# Little Professor

"""
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve.
For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

    • Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
    • Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. No need to support operations other than addition (+).
    • Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total.
      If the user has still not answered correctly after three tries, the program should output the correct answer.
    • The program should ultimately output the user’s score, a number out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with
level digits or raises a ValueError if level is not 1, 2, or 3:

def main():
        ...

def get_level():
        ...

def generate_integer(level):
    ...

"""
import random

# Main function first calls get_level() function prompting user to input a level of difficulty for the game
# Before the game begins, the score variable is set to 0. Each correct answer will increase the user's score
def main():
    level = get_level()

    score = 0

    # 10 mathematical equation questions are presented to the user during the game, each of which the user is allotted 3 attempts to solve before moving on to the next question
    # Each question calls the generate_integer() function twice, passing the user-defined level as an argument
    # 2 random integers are returned to create the mathematical equation for the question, which is then presented to the user to solve
    for round in range(10):
        attempt = 1
        generated_ints = [generate_integer(level) for x in range(2)]
        a, b = generated_ints[0], generated_ints[1]
        answer = a + b

        # If the user enters the correct answer in 3 or less attempts, 1 point is added to their score and the next question is presented
        # Otherwise, "EEE" is printed, representing an incorrect answer, and the user can try again (max of 3 tries/question)
        # If the user does not get the question correct after 3 attempts, the correct answer is printed and then the next question is presented
        while attempt < 4:
            try:
                guess = int(input(f"{a} + {b} = ").strip())
                if guess != answer:
                    print("EEE")
                    attempt += 1
                    continue

                else:
                    score += 1
                    break

            except ValueError:
                print("EEE")
                attempt += 1
                continue

        # Print correct answer, if user has not correctly answered after 3 attempts
        print(f"{a} + {b} = {answer}")

    print("Score: ", score)


# Custom function that will continue requesting the user to input a level number until they input a positive integer between 1 - 3
# Function then returns the level to the main function, which is used as a parameter when randomly generating integers for the math problems user will needs to solve
def get_level():
    while True:
        try:
            level = int(input('Level: ').strip())

            if level not in range(1, 4):
                continue

        except ValueError:
            continue

        return level

# Custom function returns a randomly generated integer with a quantity of digits equal to the level argument received
# Level 1 (1 digit numbers), Level 2 (2 digit numbers), Level 3 (3 digit numbers)
def generate_integer(level):
    if level == 1:
        generated_int = random.randint(0, 9)

    elif level == 2:
        generated_int = random.randint(10, 99)

    else:
        generated_int = random.randint(100, 999)

    return generated_int



if __name__ == "__main__":
    main()