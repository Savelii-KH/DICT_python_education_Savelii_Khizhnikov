import requests
import simplejson


if __name__ == "__main__":
    while True:
        try:
            currency = input("Enter currency code: ").lower().strip()
            r = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
            course = r.json()
            break
        except simplejson.JSONDecodeError:
            print("Incorrect currency code")
    print(f"{course['usd']['code']} to {currency.upper()} = {round(course['usd']['inverseRate'], 2)}")
    print(f"{course['eur']['code']} to {currency.upper()} = {round(course['eur']['inverseRate'], 2)}")
