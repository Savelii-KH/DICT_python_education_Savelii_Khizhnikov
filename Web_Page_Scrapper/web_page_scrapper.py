import json
import requests
from bs4 import BeautifulSoup


# https://www.imdb.com/title/tt0080684/
# https://www.imdb.com/title/tt0121766/
if __name__ == "__main__":
    url = input("Input the URL: ")
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.text, "lxml")
    if r.ok:
        try:
            description = json.loads(soup.find("script").text)
            info = {"title": description["name"], "description": description["description"]}
            print(info)
        except json.decoder.JSONDecodeError:
            print("\nInvalid quote resource!")
    else:
        print("\nInvalid quote resource!")
