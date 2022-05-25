import requests


headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79"
}

if __name__ == "__main__":
    url = input("Input the URL\n• ")
    r = requests.get(url, headers=headers)

    if r.ok:
        with open("source.html", "w", encoding="utf-8") as f:
            f.write(r.text)
        print("Content save")
    else:
        print(f"The URL returned {r.status_code}")
