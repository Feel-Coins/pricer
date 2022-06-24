import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
#Mvideo
Shop = 'Citilink'
city_code = {'_space': 'nvs_cl%3A'}
Headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'User-Agent': UserAgent().random}
Cards_teg = 'a'
Cards_class = 'ProductCardHorizontal__title'
Prices_teg = 'span'
Prices_class = 'ProductCardHorizontal__price_current-price'

def get_data():
    headers = Headers
    cookies = city_code

    response = requests.get(url='https://www.citilink.ru/catalog/videokarty/', headers=headers, cookies=cookies)

    with open(f'data from {Shop}.json', 'w') as file:
        file.write(response.text)

    with open(f'data from {Shop}.json') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all(Cards_teg, class_=Cards_class)
    prices = soup.find_all(Prices_teg, class_=Prices_class)

    prod = {}
    i, j = 0, 0
    while len(prod) < len(cards):
        card = cards[i].text.strip()
        i += 1
        price = prices[j].text.strip()
        j += 1
        prod[card] = price
    with open(f'prod_cards from {Shop}.json', 'w') as file:
        json.dump(prod, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()
