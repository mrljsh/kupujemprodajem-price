import bs4
import requests

def getKPprice(productLink):
    res = requests.get(productLink)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    priceElement = soup.select('.AdViewInfo_price__PfKUL')
    priceList = [text.strip() for text in priceElement[0].text.split(" ")]
    return priceList

price = getKPprice('https://novi.kupujemprodajem.com/casopisi-i-stripovi/stripovi-alan-ford/alan-ford/oglas/144373031')
print('Cena je: ' + ' '.join(price[1:3]))