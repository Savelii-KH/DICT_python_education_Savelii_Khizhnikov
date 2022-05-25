import os
import requests
from bs4 import BeautifulSoup


class Nature:

    def __init__(self, num_of_page: int, type_of_article: str):
        self.page = num_of_page
        self.article = type_of_article

        self.get_info()

    def __repr__(self):
        return f"Type {self.article} not found"

    def __article(self, arr):
        tran = str.maketrans(" /\'\"\\-?&!.,", "___________")
        for k in arr:
            r = requests.get(k, headers={"Accept-Language": "en-US,en;q=0.5"})
            soup = BeautifulSoup(r.text, "lxml")
            head = soup.find(class_="c-article-title").text
            texts = soup.find("div", class_="c-article-section__content").find_all("p")
            with open(f"Folder{self.page}/{head.translate(tran)}.txt", "w", encoding="utf-8") as f:
                for t in texts:
                    f.write(t.text)

    def __teaser(self, arr):
        tran = str.maketrans(" /\'\"\\-?&!.,", "___________")
        for k in arr:
            r = requests.get(k, headers={"Accept-Language": "en-US,en;q=0.5"})
            soup = BeautifulSoup(r.text, "lxml")
            head = soup.find(class_="c-article-magazine-title").text
            texts = soup.find("p", class_="article__teaser")
            with open(f"Folder{self.page}/{head.translate(tran)}.txt", "w", encoding="utf-8") as f:
                for t in texts:
                    f.write(t.text)

    def __magazine(self, arr):
        tran = str.maketrans(" /\'\"\\-?&!.,", "___________")
        for k in arr:
            r = requests.get(k, headers={"Accept-Language": "en-US,en;q=0.5"})
            soup = BeautifulSoup(r.text, "lxml")
            try:
                head = soup.find(class_="c-article-magazine-title").text
            except AttributeError:
                try:
                    head = soup.find(class_="Theme-StoryTitle Theme-TextSize-small h-align-right").text
                except AttributeError:
                    head = soup.find(class_="Theme-StoryTitle Theme-TextSize-xsmall").text
            try:
                texts = soup.find("div", class_="c-article-body u-clearfix").find_all("p")
            except AttributeError:
                try:
                    texts = soup.find(class_="Core--rootElement Theme-Story").find_all("p")
                except AttributeError:
                    texts = soup.find(class_="Core--rootElement Theme-Story").find_all("p")
            with open(f"Folder{self.page}/{head.translate(tran)}.txt", "w", encoding="utf-8") as f:
                for t in texts:
                    f.write(t.text)

    def get_info(self):
        r = requests.get(f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={self.page}", headers={"Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(r.text, "lxml")
        href = soup.find_all("a", class_="c-card__link u-link-inherit")
        types = soup.find_all("span", class_="c-meta__type")
        urls = [f"""https://www.nature.com{j["href"]}""" for j in href]
        arr = [urls[k] for k in range(len(urls)) if types[k].string == self.article]
        if self.article == "Article":
            self.__article(arr)
        elif self.article == "Author Correction":
            self.__article(arr)
        elif self.article == "Career Column":
            self.__magazine(arr)
        elif self.article == "Career Feature":
            self.__magazine(arr)
        elif self.article == "Comment":
            self.__magazine(arr)
        elif self.article == "Correspondence":
            self.__teaser(arr)
        elif self.article == "Editorial":
            self.__magazine(arr)
        elif self.article == "Futures":
            self.__magazine(arr)
        elif self.article == "Matters Arising":
            self.__article(arr)
        elif self.article == "Nature Briefing":
            self.__magazine(arr)
        elif self.article == "Nature Podcast":
            self.__magazine(arr)
        elif self.article == "News":
            self.__magazine(arr)
        elif self.article == "News & Views":
            self.__teaser(arr)
        elif self.article == "News Feature":
            self.__magazine(arr)
        elif self.article == "Outlook":
            self.__magazine(arr)
        elif self.article == "Publisher Correction":
            self.__article(arr)
        elif self.article == "Research Briefing":
            self.__teaser(arr)
        elif self.article == "Research Highlights":
            self.__teaser(arr)
        elif self.article == "Where I Work":
            self.__magazine(arr)
        elif self.article == "World View":
            self.__magazine(arr)


if __name__ == "__main__":
    while True:
        article = input("Enter type of article: ")
        try:
            num_of_pages = int(input("Enter number of pages: "))
            break
        except ValueError:
            print("Only numerical values!")
    for i in range(1, num_of_pages + 1):
        os.mkdir(f"Folder{i}")
        pars = Nature(i, article)
        if len(os.listdir(f"Folder{i}")) == 0:
            os.rmdir(f"Folder{i}")
    print("Saved all article")
