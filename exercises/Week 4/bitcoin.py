#check for the proce of bitcoin using API

import requests
import sys

def main():
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        results = response.json()["data"]
        price = float(results["priceUsd"])
        amount = get_n() * price

        print(f"${amount:,.4f}")

    except requests.RequestException:
        sys.exit(1)

def get_n():
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        n = float(sys.argv[1])
        return n

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

if __name__ == "__main__":
    main()
