# CS50P 2022 - PSET 5
# Re-requesting a Vanity Plate

"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid (still) expects a str as input and returns True if that str meets all
requirements and False if it does not, but main is only called if the value of __name__ is "__main__":
"""

# Main function requests user input for a vanity license plate, removes leading/trailing spaces and sets value equal to plate variable
# A custom function is then called on the plate variable to determine if user input was valid or invalid
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# def is_valid(s):
#     if s[0:2].isalpha() and (2 <= len(s) <= 6) and s.isalnum():
#         return True


# Custom boolean function returns True only if input has passed all requirements
# Each requirement is defined in its own custom function below. is_valid(s) function only returns True if all other functions returned True
def is_valid(s):
    if valid_length(s) and valid_first_two(s) and valid_characters(s) and valid_numbers(s):
        return True
    else:
        return False


# Custom boolean function checks first 2 characters of input and returns True only if they are letters
def valid_first_two(s):
    if s[0:1].isalpha():
        # print("First 2 is alpha")
        return True
    else:
        # print("First 2 is NOT alpha")
        return False


# Custom boolean function checks qty of characters and returns True only if qty is between 2 - 6
def valid_length(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True


# Custom boolean function checks all characters of input and returns True only if they are all alphanumeric
def valid_characters(s):
    if s.isalnum():
        return True
    else:
        return False


# Custom boolean function to determine if numbers were used properly, if at all
def valid_numbers(s):

    # Return True if s only contains letters
    if s.isalpha():
        return True

    # If s does not only contain letters and s is greater than 2 characters in length, evaluate the rest of the characters in s (after the first 2) to determine if numbers
    # were used properly
    elif len(s) > 2:
        index = 2
        s_slice = s[index:]

        # Before checking for numbers, check characters for a zero. Since zero can't appear before another non-zero digit, the plate will be invalid if a zero is found in this step
        for character in s_slice:
            if character == "0":
                return False

            # If character is not a zero, check if it's a non-zero digit. If a non-zero digit is found, only digits (including zero) may follow it.
            # Once a non-zero digit is found, need to evaluate the slice of the string that follows that digit. Create a second slice for this step
            elif character.isdigit() and character != "0":
                index += 1
                second_slice = s_slice[index:]

                # Loop through characters of second slice and return false if a letter is found
                for next_character in second_slice:
                    if next_character.isalpha():
                        return False

                # All numerical tests have passed. Return True
                return True

if __name__ == "__main__":
    main()