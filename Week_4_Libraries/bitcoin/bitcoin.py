# CS50P 2022 - PSET 4
# Bitcoin Price Index

"""
Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network,
otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

    • Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
    • Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
    • Outputs the current cost of  Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import sys
import requests

# Main function first checks command-line arguments to ensure user has input a valid numeric input representing the qty of Bitcoin to convert to USD. Otherwise, program will exit and display exception error
# Function then calls bitcoin_price() function, passing user input qty as an argument
# Finally, function calculates total USD cost of n bitcoin and prints in proper format

def main():
    try:
        qty = float(sys.argv[1])

    except IndexError:
        sys.exit("Missing command-line argument")

    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = bitcoin_price(qty)

    transaction_total = price * qty
    print("${:,.4f}".format(transaction_total))

# Custom function makes an API call to CoinDesk to retrieve current price of Bitcoin in USD
# CoinDesk's API returns JSON response, which is then parsed for the current price of Bitcoin in USD
# If no exceptions occur, function returns current price to main() 
def bitcoin_price(qty):

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        r = requests.get(url)
        response = r.json()
        price = ((response["bpi"])["USD"])["rate_float"]

    except requests.RequestException:
        sys.exit("There was a problem.")

    return price

if __name__ == "__main__":
    main()