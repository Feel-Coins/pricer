# scraper for citilink.ru
import requests
import re
# import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import psycopg2
import datetime

page = 1
# 'processory', 'videokarty', 'materinskie-platy', , 'bloki-pitaniya', 'korpusa'
device = ['processory', 'videokarty', 'materinskie-platy', 'moduli-pamyati', 'bloki-pitaniya', 'korpusa']
device_counter = 0
data_page = 0


# creating database
date_string = datetime.datetime.now()
now = str(date_string.strftime('%d%m%y%H%M'))
connection = psycopg2.connect('dbname=Pricer user=postgres')
cursor = connection.cursor()
cursor.execute(f'create table citilink_{now}'
               f'(id serial primary key, class varchar, product_name varchar, price integer, link varchar);')
connection.commit()


def get_data(city_code='nvs_cl%3A'):
    global data_page, device_counter, device, now, connection, cursor
    ua = UserAgent()

    #get response
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

    #writing html
    with open(f'data from citilinks page {page}.json', 'w') as file:
        file.write(response.text)

    with open(f'data from citilinks page {page}.json') as file:
        src = file.read()

    #soup the data
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

    #page counter
    int_page = []
    if page == 1:
        for each_page in num_of_pages:
            try:
                int_page.append(int((each_page.text.strip())))
            except:
                pass
            data_page = max(int_page)
        print(f'In {device[device_counter]} citilink have {data_page} pages')

    card_list = []
    price_list = []
    link_list = []

    # preparing data to collect
    for card in cards:
        card_link = card.get('href')
        card = card.text.strip()
        card_list.append(card)
        link_list.append('https://www.citilink.ru' + card_link)
        if device[device_counter] == 'moduli-pamyati':
            card_list.append(card)
            link_list.append('https://www.citilink.ru' + card_link)
        else:
            pass
    for price in current_prices:
        if device[device_counter] == 'moduli-pamyati':
            price = int(price.text.strip().replace(' ', ''))
            price_list.append(price)
        else:
            price = int(price.text.strip().replace(' ', ''))
            price_list.append(price)

    # print progress
    print(f'{page}/{data_page} pages \nPlease stand by...')
    print(len(card_list), len(price_list), len(link_list))

    #collect info in set
    result = set(zip(card_list, price_list, link_list))
    #writing to file.json
    # with open(f' citilinks {device[device_counter]}.json', 'a') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    #writing to DB
    for card in result:
        cursor.execute(f'insert into citilink_{now}(product_name, price, class, link) values (%s, %s, %s, %s)',
                       (card[0], card[1], device[device_counter], card[2]))


def main():
    global page, device_counter, data_page

    #walking on products and getting data from all pages
    while device_counter != len(device):
        data_page = page = 1
        while page <= data_page:
            get_data()
            page += 1
        print('\n\n')
        device_counter += 1
    print('Parcing complete!')

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
