# scraper for citilink.ru
import requests
import re
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

page = 1
device = ['moduli-pamyati']
device_counter = 0
data_page = 0
# 'processory', 'videokarty', 'materinskie-platy', , 'bloki-pitaniya', 'korpusa'


def get_data(city_code='nvs_cl%3A'):
    global data_page, device_counter, device
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

    response = requests.get(url=f'https://www.citilink.ru/catalog/{device[device_counter]}/?p={page}', headers=headers,
                            cookies=cookies)

    with open(f'data from citilinks page {page}.json', 'w') as file:
        file.write(response.text)

    with open(f'data from citilinks page {page}.json') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    if device[device_counter] == 'moduli-pamyati':
        cards = soup.find_all('a', class_='ProductCardVertical__name')
    else:
        cards = soup.find_all('a', class_='ProductCardHorizontal__title')

    if device[device_counter] == 'moduli-pamyati':
        current_prices = soup.find_all('span', class_='ProductCardVerticalPrice__price-current_current-price '
                                                      'js--ProductCardVerticalPrice__price-current_current-price')
    else:
        current_prices = soup.find_all('span', class_='ProductCardHorizontal__price_current-price')

    num_of_pages = soup.find_all('a', class_=(re.compile('PaginationWidget__page js--PaginationWidget__page')))
    cards = list(cards)
    current_prices = list(current_prices)

    if data_page == 1:
        data_page = len(num_of_pages)
    else:
        pass
    print(f'In {device[device_counter]} citilink have {data_page} pages')

    card_list = []
    price_list = []

    for card in cards:
        card = card.text.strip()
        card_list.append(card)

    for price in current_prices:
        if device[device_counter] == 'moduli-pamyati':
            price = price.text.strip()
            if price in price_list:
                price_list.append(price)
        else:
            price = price.text.strip()
            price_list.append(price)

    print(f'Page {page} is ready. Parsed {device[device_counter]} and their prices \nPlease stand by...')
    print(len(card_list), len(price_list))

    result = dict(zip(card_list, price_list))

    with open(f' citilinks {device[device_counter]}.json', 'a') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    global page, device_counter, data_page

    while device_counter != len(device):
        data_page = page = 1
        while page <= data_page:
            get_data()
            page += 1
        device_counter += 1
    print('Parcing complete!')


if __name__ == '__main__':
    main()
