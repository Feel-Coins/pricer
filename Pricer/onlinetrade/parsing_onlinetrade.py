# scraper for onlinetrade.ru
import requests
import re
# import json
from bs4 import BeautifulSoup
from time import sleep
import psycopg2
import datetime

print("""
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████▌▐█████████████████████████
███████▀▀▀████▀▀██▀▀██▀▀▀▀▀▀███▀▀████▀▀▄▄▀▀██▀▀██▀▀██▌▐█████████████████████████
█████▌  ▄▄  █▌  ██  ██  ▄   ██    ██▌ ▐█   █▌  ██  ██▌▐██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████
█████  ▐██  █▌  ▄▄  ██  █▌  █▌ ▀   █▌   ▄  █▌  ▄▄  ██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████
██████▄    ▄█▌ ▐██  █  ▄█▌  █  ▄▄  ▐▌  ██  █▌  ██  ██  ██▓   ▄   ▓▓   ▓   ▓█████
█████████████████████████████████████████████████████▄▄███   ▓▓   ▓▓  ▓   ▓█████
███████████████████████████████▀▀▀█▀▀▀█▀▀▀██▄▄███▀▀██▀▀██▓   ▓▀  ▐▓▓     ▓▓█████
████████████████████████████████ ██ ▀▀▐ ▀▀█ █▀ █ █ ██  ██▓      ▓▓▓▓▓   ▓▓▓█████
████████████████████████████████ ██ ███ ▀▀█ ▄█ ▌ ▀ ▀█  ██▓   ▓▓▓▓▓▓   ▓▓▓▓▓█████
█████████████████████████████████████████████████████▌▐██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████
█████████████████████████████████████████████████████▌▐█████████████████████████
█████████████████████████████████████████████████████▌▐█████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
`""")

page = 0
# 'videokarty-c338', 'materinskie_platy-c340', 'operativnaya_pamyat-c341', 'bloki_pitaniya-c339', 'protsessory-c342', 'kompyuternye_korpusa-c1323'
category_list = ['protsessory-c342', 'videokarty-c338', 'materinskie_platy-c340', 'operativnaya_pamyat-c341', 'bloki_pitaniya-c339']
category_index = 0
max_pages = 0

# creating database
date_now = datetime.datetime.now()
now_str = str(date_now.strftime('%d%m%y%H%M'))
connection = psycopg2.connect('dbname=Pricer user=postgres')
cursor = connection.cursor()
cursor.execute(f'create table onlinetrade_{now_str}'
               f'(id serial primary key, class varchar, product_name varchar, price integer, link varchar);')
connection.commit()


def get_data():
    global max_pages, category_index, category_list, now_str, connection, cursor

    # get response
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/'
                      '89.0.4447.48 (Edition Yx 05)',

        'Cookie': 'spst=1655708945664_2e51f3bb090a42993af0555ea09f57ea_b350434491ba66d4f19a71c5c6917fb3; '
                  'spsn=1655708943776_7b2276657273696f6e223a22332e332e33222c227369676e223a2230376464663864383966393064616233633765373331613336646234'
                  '66663538222c22706c6174666f726d223a2257696e3332222c2262726f7773657273223a5b226368726f6d65225d2c2273636f7265223a302e367d;'
                  'spid=1655708943776_915414789ec9af183d6a83eeec7cfbca_euleln6xqsxlijip; _ym_uid=16557089571012159871; _ym_d=1655708957;'
                  '_gcl_au=1.1.1908999290.1655708957; spsc=1655798501915_4e1fc4fb32bc831a33c9b288d0852324_a5476469b72f558bb72e6aae99c6a060;'
                  'session_id=71564aab774da2bce16642661afc8909; '
                  '__utmc=77444427; __utmz=77444427.1658221688.1.1.utmcsr=yandex.ru|utmccn=(referral)|utmcmd=referral|utmcct=/;'
                  '_ga=GA1.2.298689962.1658221688;'
                  # City and item per page
                  'user_city=24; user_c=52; items_per_page=45;'
                  'onlinetrade=c261b65830ff5ee0c0f519c09a71549b; '
                  'views=1065420,1864402,698439,1153906,1838255,918624,1952400,2008374,2094253,1689399;'
                  '__utma=77444427.298689962.1658221688.1658483004.1658728520.6; _ym_isad=2; _ym_visorc=w; b=1f1b081e6e52d6ea53ba5f2b23c68ac6',

        'Host': 'www.onlinetrade.ru'

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
    print(f'{page + 1} page \nPlease stand by...')
    print(f'{len(card_list)} names, {len(price_list)} prices, {len(link_list)} links \n')

    # collect info in set
    result = set(zip(card_list, price_list, link_list))

    # writing to file.json
    # with open(f' citilinks {category_list[category_index]}.json', 'a') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    # writing to DB
    for card in result:
        cursor.execute(f'insert into onlinetrade_{now_str}(product_name, price, class, link) values (%s, %s, %s, %s)',
                       (card[0], card[1], category_list[category_index[:-4]], card[2]))

    connection.commit()


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
    print('Parcing complete! \nYou may close the window.')
    sleep(300)

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
