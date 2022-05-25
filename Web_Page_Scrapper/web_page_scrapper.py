import requests


if __name__ == "__main__":
    url = input("Input the URL: ")
    r = requests.get(f"{url}")
    if r.ok:
        print(f"""\n{r.json()["content"]}""")
    else:
        print("\nInvalid quote resource!")
