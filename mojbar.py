from pprint import pprint

from main import get_urls, scrape_drink_name, scrape_drink_prepare, scrape_drink_prepare2, scrape_drink_ingred
from main import Drink, Bar

url = "https://mojbar.pl/drinki-z-wodka/"

url_details = "https://mojbar.pl/long-island-iced-tea-przepis-na-drink/"

urls = get_urls(url)

for e, url in enumerate(urls, start=1):
    print(f"{e} : {scrape_drink_name(url)} --> {scrape_drink_prepare2(url)}")
    # print(f"{e} : {scrape_drink_prepare2(url)}")
    # a = [scrape_drink_name(url), scrape_drink_ingred(url), scrape_drink_prepare(url)]
    # total = Bar([])
    # print(a)

# print(scrape_drink_name(url_details))
# print(scrape_drink_ingred(url_details))
# pprint(scrape_drink_prepare2("https://mojbar.pl/harvey-wallbanger-przepis-na-drink/"))



