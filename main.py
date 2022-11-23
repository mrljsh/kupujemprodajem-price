import bs4
import requests

def getKPprice(productLink):
    res = requests.get(productLink)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    priceElement = soup.select('.AdViewInfo_price__PfKUL');
    return priceElement[0].text.strip()[6:]

price = getKPprice('https://novi.kupujemprodajem.com/kompjuteri-laptop-i-tablet/laptopovi/thinkpad-t14-14-fhd-i5-10th-16gb-256nvme-garancija/oglas/143348543')
print(price)