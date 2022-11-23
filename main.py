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


price = getKPprice('https://novi.kupujemprodajem.com/')
if price:
    print('Cena je: ' + ' '.join(price[1:3]))
