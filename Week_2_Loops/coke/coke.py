# CS50P 2022 - PSET 2
# Coke

"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore
any integer that isn’t an accepted denomination.
"""

# Define a main function that asks a user to pay the balance due for their Coke
def main():
    # Assign the value of 50 to the balance variable, then inform the user of the initial balance due for their Coke.
    balance = int(50)
    payment = 0
    change = 0
    print("Amount Due: ", balance)

    # Continue the below process as long as there is a balance due for the Coke
    # Request user to input the value of a coin
    # If user correctly inputs values (25, 10 or 5), call the transaction function to re-calculate the balance. Otherwise, re-prompt the user for input
    # After each coin is inserted, notify the user what the new balance is
    while balance > 0:
        payment = int(input("Insert Coin: "))
        if payment == int(25) or payment == int(10) or payment == int(5):
            balance = transaction(balance, payment)
        if balance > 0:
            print("Amount Due: ", balance)

    # If user has insert exact change (no balance and no change due), print "0"
    if balance == 0:
        print("0")

    # Otherwise, multiply the negative balance by -1, assign value to change variable and let the user know how much change they are owed
    else:
        change = balance * -1
        print("Change Owed: ", change)

# Custom function used to re-calculate the balance after each coin is inserted
def transaction(balance, payment):
    return (balance - payment)

if __name__ == "__main__":
    main()