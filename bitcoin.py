import requests
import sys


try:
    text = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.JSONDecodeError:
    sys.exit(1)

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


b_price = text["bpi"]["USD"]["rate_float"]
amount = b_price * bitcoins

print(f"${amount:,.4f}")
