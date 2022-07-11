# scraper for citilink.ru
import requests
import re
# import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import psycopg2
import datetime

page = 1
# 'processory', 'videokarty', 'materinskie-platy', 'moduli-pamyati', 'bloki-pitaniya', 'korpusa'
category_list = ['processory', 'videokarty', 'materinskie-platy', 'moduli-pamyati', 'bloki-pitaniya', 'korpusa']
category_index = 0
max_pages = 0


# creating database
date_now = datetime.datetime.now()
now_str = str(date_now.strftime('%d%m%y%H%M'))
connection = psycopg2.connect('dbname=Pricer user=postgres')
cursor = connection.cursor()
cursor.execute(f'create table citilink_{now_str}'
               f'(id serial primary key, class varchar, product_name varchar, price integer, link varchar);')
connection.commit()


def get_data(city_code='nvs_cl%3A'):
    global max_pages, category_index, category_list, now_str, connection, cursor
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

    response = requests.get(url=f'https://www.citilink.ru/catalog/{category_list[category_index]}/?p={page}',
                            headers=headers, cookies=cookies)

    #writing html
    with open(f'data from citilinks page {page}.json', 'w') as file:
        file.write(response.text)

    with open(f'data from citilinks page {page}.json') as file:
        src = file.read()

    #soup the data
    soup = BeautifulSoup(src, 'lxml')
    if category_list[category_index] == 'moduli-pamyati':
        card_title = soup.find_all('a', class_='ProductCardVertical__name')
    else:
        card_title = soup.find_all('a', class_='ProductCardHorizontal__title')
    if category_list[category_index] == 'moduli-pamyati':
        current_prices = soup.find_all('span', class_='ProductCardVerticalPrice__price-current_current-price '
                                                      'js--ProductCardVerticalPrice__price-current_current-price')
    else:
        current_prices = soup.find_all('span', class_='ProductCardHorizontal__price_current-price')

    page_count = soup.find_all('a', class_=(re.compile('PaginationWidget__page js--PaginationWidget__page')))
    product_name_list = list(card_title)
    current_prices_list = list(current_prices)

    #page counter
    page_list = []
    if page == 1:
        for each_page in page_count:
            try:
                page_list.append(int((each_page.text.strip())))
            except:
                pass
            max_pages = max(page_list)
        print(f'In {category_list[category_index]} citilink have {max_pages} pages')

    card_list = []
    price_list = []
    link_list = []

    # preparing data to collect
    for card in product_name_list:
        card_link = card.get('href')
        card_name = card.text.strip()
        card_list.append(card_name)
        link_list.append('https://www.citilink.ru' + card_link)
        if category_list[category_index] == 'moduli-pamyati':
            card_list.append(card_name)
            link_list.append('https://www.citilink.ru' + card_link)
        else:
            pass
    for price in current_prices_list:
        if category_list[category_index] == 'moduli-pamyati':
            price = int(price.text.strip().replace(' ', ''))
            price_list.append(price)
        else:
            price = int(price.text.strip().replace(' ', ''))
            price_list.append(price)

    # print progress
    print(f'{page}/{max_pages} pages \nPlease stand by...')
    print(f'{len(card_list)} names, {len(price_list)} prices, {len(link_list)} links')

    #collect info in set
    result = set(zip(card_list, price_list, link_list))

    #writing to file.json
    # with open(f' citilinks {category_list[category_index]}.json', 'a') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    #writing to DB
    for card in result:
        cursor.execute(f'insert into citilink_{now_str}(product_name, price, class, link) values (%s, %s, %s, %s)',
                       (card[0], card[1], category_list[category_index], card[2]))


def main():
    global page, category_index, max_pages

    #walking on products and getting data from all pages
    while category_index != len(category_list):
        max_pages = page = 1
        while page <= max_pages:
            get_data()
            page += 1
        print('\n\n')
        category_index += 1
    print('Parcing complete!')

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
