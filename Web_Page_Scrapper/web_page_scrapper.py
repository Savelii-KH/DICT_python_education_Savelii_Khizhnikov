import requests
from bs4 import BeautifulSoup


URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.5",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79"
}

if __name__ == "__main__":
    r1 = requests.get(URL, headers=HEADERS)
    soup1 = BeautifulSoup(r1.text, "lxml")

    href = soup1.find_all("a", class_="c-card__link u-link-inherit")
    types = soup1.find_all("span", class_="c-meta__type")

    urls = [f"""https://www.nature.com{i["href"]}""" for i in href]
    news = [urls[i] for i in range(len(urls)) if types[i].string == "News"]

    for i in news:
        r2 = requests.get(i, headers=HEADERS)
        soup2 = BeautifulSoup(r2.text, "lxml")

        head = soup2.find(class_="c-article-magazine-title").text.replace(" ", "_")
        text = soup2.find("div", class_="c-article-body u-clearfix").find_all("p")

        with open(f"{head}.txt", "w", encoding="utf-8") as f:
            for t in text:
                f.write(t.text)
    print("File saved")
