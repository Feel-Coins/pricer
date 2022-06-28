# scraper for citilink.ru
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

page = 1


def get_data(city_code = 'nvs_cl%3A'):
    ua = UserAgent()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    #change cookies "'_space': 'nvs_cl%3A'" to change city
    cookies = {
        '_space': f'{city_code}'
    }

    response = requests.get(url=f'https://www.citilink.ru/catalog/videokarty/?p={page}', headers=headers, cookies=cookies)

    with open(f'data from citilinks page {page}.json', 'w') as file:
        file.write(response.text)

    with open(f'data from citilinks page {page}.json') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='ProductCardHorizontal__title')
    current_prices = soup.find_all('span', class_='ProductCardHorizontal__price_current-price')

    cards = list(cards)
    current_prices = list(current_prices)

    card_list = []
    price_list = []

    for card in cards:
        card = card.text.strip()
        card_list.append(card)
    for price in current_prices:
        price = price.text.strip()
        price_list.append(price)

    print(f'Page {page} is ready. Parsed titles and prices: ')
    print(len(card_list), len(price_list))

    result = dict(zip(card_list, price_list))

    with open(f'product card citilinks page {page}.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    global page
    while page <= 3:
        get_data()
        page += 1


if __name__ == '__main__':
    main()
