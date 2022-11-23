import bs4
import requests

def getKPprice(productLink):
    res = requests.get(productLink)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    priceElement = soup.select('.AdViewInfo_price__PfKUL')
    if priceElement:
        priceList = [text.strip() for text in priceElement[0].text.split(" ")]
        return priceList
    else:
        print("Greska, cena nije pronadjena. Proverite da li je link ispravan.")
        return


price = getKPprice('https://novi.kupujemprodajem.com/')
if price:
    print('Cena je: ' + ' '.join(price[1:3]))
