import bs4
import requests


def getKPprice(product_link):
    res = requests.get(product_link)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    price_element = soup.select('.AdViewInfo_price__PfKUL')

    if price_element:
        price_list = [text.strip() for text in price_element[0].text.split(" ")]
        return price_list
    else:
        print("Greska, cena nije pronadjena. Proverite da li je link ispravan.")
        return


class Ad:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price})"

    def __repr__(self):
        return str(self)


def get_kp_category_prices(category_link):
    res = requests.get(category_link)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    ad_list = []

    without_price_list = ["Kontakt", "Besplatno", "Dogovor", "Pozvati", "Kupujem", "-"]

    for container in soup.find_all('article', 'AdItem_adHolder__GL0yo'):
        ad_name = container.select(
            '.AdItem_descriptionHolder__xnkD4 > .AdItem_adInfoHolder___36KR > .AdItem_adTextHolder__lNoRA  '
            '.AdItem_name__BppRQ')

        price = container.select(
            '.AdItem_descriptionHolder__xnkD4 > .AdItem_priceHolder__DUd47 > div > .AdItem_price__k0rQn')

        if price[0].text in without_price_list:
            continue

        ad_list.append(Ad(ad_name[0].text, price[0].text))

    print(ad_list)

    return ad_list
    #


#
# def avg_price(ad_list):
#     for item in ad_list:
#         if item.price ==


#
# price = getKPprice('https://novi.kupujemprodajem.com/')
# if price:
#     print('Cena je: ' + ' '.join(price[1:3]))

get_kp_category_prices('https://novi.kupujemprodajem.com/pretraga?keywords=iphone')
