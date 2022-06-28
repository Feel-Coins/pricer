# scraper for citilink.ru
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_data(city_code = 'nvs_cl%3A'):
    ua = UserAgent()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }
    #change cookies "'_space': 'nvs_cl%3A'" to change city
    cookies = {
        '_space': f'{city_code}'
    }

    response = requests.get(url='https://www.citilink.ru/catalog/videokarty/', headers=headers, cookies=cookies)

    # with open('data.json', 'w') as file:
    #     file.write(response.text)

    with open('data.json') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='ProductCardHorizontal__title')
    current_prices = soup.find_all('span', class_='ProductCardHorizontal__price_current-price')

    cards = list(cards)
    current_prices = list(current_prices)
    print(cards)
    print(current_prices)
    print(len(cards))
    print(len(current_prices))

    card_list = []
    price_list = []

    for card in cards:
        card = card.text.strip()
        card_list.append(card)
    for price in current_prices:
        price = price.text.strip()
        price_list.append(price)

    print(len(card_list), len(price_list))
    result = dict(zip(card_list, price_list))

    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()
