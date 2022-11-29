import kp_scraper as kp

print('[1] Cena pojedinacnog oglasa')
print('[2] Prosecna cena kategorije pretrage')
choice = input("Unesite izbor: ")

if choice == "1":
    print('Unesite link pojedinacnog oglasa - (primer linka: https://novi.kupujemprodajem.com/kategorija/podkategorija/ime-oglasa/oglas/id)')
    link = input('URL: ')
    price = kp.getKPprice(link)
    if price:
        print('Cena je: ' + price)
elif choice == "2":
    print('Unesite link pretrage - (primer linka: https://novi.kupujemprodajem.com/kategorija/podkategorija/pretraga')
    print('Za preciznije podatke, uneti link detaljne pretrage (stanje, mesto...)')
    link = input('URL: ')
    ad_list = kp.get_kp_category_prices(link)
    average_rsd = kp.avg_price_rsd(ad_list)
    average_eur = kp.rsd_to_eur(average_rsd)
    print('Prosecna cena je ' + str(average_rsd) + 'RSD ( ' + str(average_eur) + '€ )')
else:
    print("Greska pri izboru")