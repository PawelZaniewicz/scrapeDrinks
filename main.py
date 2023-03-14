from dataclasses import dataclass
from typing import List
from bs4 import BeautifulSoup
import requests

url = "https://mojbar.pl/drinki-z-wodka/"


@dataclass
class Drink():
    name: str
    ingredients: List[str]
    recipe: str


@dataclass
class Bar():
    drinks: List[Drink]


#
# a = Drink("Wódka", ["20 ml ginu", "20 ml jasnego rumu", "20ml soku z cytryny"],
#           "Wszystko wymieszać dokladnie w shakerze.")
#
# print(a)


def get_categories(url: str):
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    www_categories = soup.findAll("div", attrs={"class": "td-module-meta-info"})

    list_categories = []
    for row in www_categories:
        data = row.findAll("a")
        for n, val in enumerate(data):
            list_categories.append(val.text.strip())

    return list_categories


def get_urls(url: str):
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    www_urls = soup.findAll("h3", attrs={"class": "entry-title"})

    list_urls = []
    for row in www_urls:
        data = row.find_all('a', href=True)
        # print(data)
        for n, a in enumerate(data):
            list_urls.append((a['href']))

    return list_urls


def scrape_drink_name(urls: str):
    page_to_scrape = requests.get(urls)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    _contents = soup.findAll("div", attrs={"class": "tdb-block-inner td-fix-index"})

    for row in _contents:
        name = row.find("h2")
        if name:
            return name.text


def scrape_drink_ingred(urls: str):
    page_to_scrape = requests.get(urls)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    _contents = soup.findAll("div", attrs={"class": "tdb-block-inner td-fix-index"})
    ing = []

    for row in _contents:
        name = row.find("h2")
        ingred = row.find_all(lambda txt: len(txt.find_all()) == 0 and "ml" in txt.text)

        if ingred:
            for i in ingred:
                ing.append(i.text)
            return ing


def scrape_drink_prepare(urls: str):
    page_to_scrape = requests.get(urls)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    _preparation = soup.findAll("p")
    _p = _preparation[1].text
    _preparation = _p[22:]

    return _preparation


def scrape_drink_prepare2(urls: str):
    page_to_scrape = requests.get(urls)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    _preparation = soup.findAll("p")

    lista = [a for a in _preparation]

    return lista[2::1]

# def scrape_content_from_drink(urls: str):
#     page_to_scrape = requests.get(urls)
#     soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
#
#     _contents = soup.findAll("div", attrs={"class": "tdb-block-inner td-fix-index"})
#     _preparation = soup.findAll("p")
#     _p = _preparation[1].text
#     _preparation = _p[22:]
#
#     for row in _contents:
#         name = row.find("h2")
#         ingred = row.find_all(lambda txt: len(txt.find_all()) == 0 and "ml" in txt.text)
#
#         if name and ingred:
#             print(f"Nazwa: {name.text}")
#             for sklad in ingred:
#                 print(f"Składniki: {sklad.text}")
#     print(_preparation)
