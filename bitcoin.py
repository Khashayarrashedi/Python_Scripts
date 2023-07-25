import sys
import requests
import json

def main():
    try:
        if len(sys.argv)==1:
            sys.exit("Missing command-line argument")
        ordered_bitcoin= float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        pass

    #------------ so it means user entered a number correctly
    #------------ now we should change it to dollor based on BC price
    try:
        response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response=response.json()
    except requests.RequestExceptions:
        sys.exit("Request Error")
    else:
        pass

    #--- addressing the rate_float according to the response file structure
    bitcoin_rate= response["bpi"]["USD"]["rate_float"]
    Total_price = float(sys.argv[1])*bitcoin_rate
    print(f"${Total_price:,.4f}")

if __name__ == "__main__":
    main()