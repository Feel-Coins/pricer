# scraper for citilink.ru
import requests
import re
# import json
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent
import psycopg2
import datetime

page = 0
# 'videokarty-c338', 'materinskie_platy-c340', 'operativnaya_pamyat-c341', 'bloki_pitaniya-c339', 'kompyuternye_korpusa-c1323' 'protsessory-c342'
category_list = ['protsessory-c342', 'videokarty-c338', 'materinskie_platy-c340', 'operativnaya_pamyat-c341', 'bloki_pitaniya-c339',
                 'kompyuternye_korpusa-c1323']
category_index = 0
max_pages = 0

# creating database
date_now = datetime.datetime.now()
now_str = str(date_now.strftime('%d%m%y%H%M%S'))
connection = psycopg2.connect('dbname=Pricer user=postgres')
cursor = connection.cursor()
cursor.execute(f'create table onlinetrade_{now_str}'
               f'(id serial primary key, class varchar, product_name varchar, price integer, link varchar);')
connection.commit()


def get_data():
    global max_pages, category_index, category_list, now_str, connection, cursor
    ua = UserAgent()

    # get response
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',

        'User-Agent': ua.random,
        'cookie': 'user_city=24; user_c=52; items_per_page=45;'
    }

    response = requests.get(url=f'https://www.onlinetrade.ru/catalogue/{category_list[category_index]}/?page={page}',
                            headers=headers)

    # writing html
    with open(f'data from onlinetrades page {page + 1}.json', 'w') as file:
        file.write(response.text)

    with open(f'data from onlinetrades page {page + 1}.json') as file:
        src = file.read()

    # soup the data
    soup = BeautifulSoup(src, 'lxml')
    card_title = soup.find_all('a', class_=(re.compile('indexGoods__item__name')))
    current_prices = soup.find_all('span', class_='js__actualPrice')

    page_counter = soup.find('div', class_='paginator__links')
    page_count = page_counter.find_all(re.compile('a'))

    product_name_list = list(card_title)
    current_prices_list = list(current_prices)

    # page counter
    page_list = []
    for each_page in page_count:
        try:
            page_list.append(int((each_page.text.strip())))
            max_pages = max(page_list)
        except:
            pass
    print(f'In {category_list[category_index]} onlinetrade we found {max_pages} pages')

    card_list = []
    price_list = []
    link_list = []

    # preparing data to collect
    for card in product_name_list:
        card_link = card.get('href')
        card_name = card.text.strip()
        card_list.append(card_name)
        link_list.append('https://www.onlinetrade.ru' + card_link)

    for price in current_prices_list:
        price = int(price.text.strip().replace(' ', '').replace('₽', ''))
        price_list.append(price)

    # print progress
    print(f'{page + 1}/{max_pages} pages \nPlease stand by...')
    print(f'{len(card_list)} names, {len(price_list)} prices, {len(link_list)} links \n')

    # collect info in set
    result = set(zip(card_list, price_list, link_list))

    # writing to file.json
    # with open(f' citilinks {category_list[category_index]}.json', 'a') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    # writing to DB
    for card in result:
        cursor.execute(f'insert into onlinetrade_{now_str}(product_name, price, class, link) values (%s, %s, %s, %s)',
                       (card[0], card[1], category_list[category_index], card[2]))


def main():
    global page, category_index, max_pages

    # walking on products and getting data from all pages
    while category_index != len(category_list):
        max_pages = page = 0
        while page <= max_pages:
            get_data()
            page += 1
            sleep(1)
        print('\n\n')
        category_index += 1
    print('Parcing complete!')

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
