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

def get_kp_category_prices(category_link):
    res = requests.get(category_link)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    for container in soup.find_all('article', 'AdItem_adHolder__GL0yo'):
        ad_name = container.select('.AdItem_descriptionHolder__xnkD4 > .AdItem_adInfoHolder___36KR > .AdItem_adTextHolder__lNoRA  .AdItem_name__BppRQ')
        price = container.select('.AdItem_descriptionHolder__xnkD4 > .AdItem_priceHolder__DUd47 > div > .AdItem_price__k0rQn')
        print(price[0].text + " - " + ad_name[0].text)

    #
    # print(price_container[0].text)


#
# price = getKPprice('https://novi.kupujemprodajem.com/')
# if price:
#     print('Cena je: ' + ' '.join(price[1:3]))

get_kp_category_prices('https://novi.kupujemprodajem.com/pretraga?keywords=thinkpad%20t14')