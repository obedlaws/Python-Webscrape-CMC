from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://coinmarketcap.com/new/').text
soup = BeautifulSoup(html_text, 'lxml')


allcoins = soup.find('table', class_ ="h7vnx2-2 deceFm cmc-table")

coin_name = soup.find_all('p', class_ = "sc-1eb5slv-0 iworPT")

sourceFile = open('coin_name.txt', 'w')
for names in coin_name:
    print(names.text, file = sourceFile)
sourceFile.close()

coin_abv = allcoins.find_all('p', class_ = "sc-1eb5slv-0 gGIpIK coin-item-symbol")

sourceFile = open('coin_symbols.txt', 'w')
for i in coin_abv:
    print(i.text, file = sourceFile)
sourceFile.close()

price_cap_volume = allcoins.find_all(text=lambda text: text and '$' in text)

sourceFile = open('price_cap_volume.txt', 'w')
for price in price_cap_volume:
    print(price, file = sourceFile)
sourceFile.close()


# debugging/testing
# print()