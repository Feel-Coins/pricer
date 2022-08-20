from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re
from selenium.webdriver.common.by import By
import psycopg2
import datetime

# create road map for parser
page = 0
# 'protsessory-c342', 'videokarty-c338', 'materinskie_platy-c340', 'operativnaya_pamyat-c341', 'bloki_pitaniya-c339', 'kompyuternye_korpusa-c1323'
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

# open browser
driver = webdriver.Chrome()
driver.maximize_window()


def parser():
    global max_pages, category_index, category_list, now_str, connection, cursor

# open sourse
    driver.get(f'https://www.onlinetrade.ru/catalogue/{category_list[category_index]}/?page={page}&per_page=45')
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

# checking block
    if soup.find('input', class_='button button__orange size18'):
        driver.find_element(By.ID, 'otv3_submit').click()
        sleep(1)
        driver.get(f'https://www.onlinetrade.ru/catalogue/{category_list[category_index]}/?page={page}&per_page=45')
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
    else:
        pass

# souping the data
    card_title = soup.find_all('a', class_=(re.compile('indexGoods__item__name')))
    current_prices = soup.find_all('span', class_='js__actualPrice')
    product_name_list = list(card_title)
    current_prices_list = list(current_prices)


# page counter
    page_list = []
    page_finder = soup.find('div', class_='paginator__links')
    page_count = page_finder.find_all(re.compile('a'))
    for each_page in page_count:
        try:
            page_list.append(int((each_page.text.strip())))
            max_pages = max(page_list)
        except:
            pass
    print(f'In {category_list[category_index]} onlinetrade we found {max_pages} pages')

# preparing data to collect
    name_list = []
    price_list = []
    link_list = []

    for card in product_name_list:
        card_link = card.get('href')
        card_name = card.text.strip()
        name_list.append(card_name)
        link_list.append('https://www.onlinetrade.ru' + card_link)

    for price in current_prices_list:
        price = int(price.text.strip().replace(' ', '').replace('₽', ''))
        price_list.append(price)

# print progress
    print(f'{page + 1} page \nPlease stand by...')
    print(f'{len(name_list)} names, {len(price_list)} prices, {len(link_list)} links \n')

# collect info in set
    result = set(zip(name_list, price_list, link_list))

# writing to DB
    for card in result:
        cursor.execute(f'insert into onlinetrade_{now_str}(product_name, price, class, link) values (%s, %s, %s, %s)',
                       (card[0], card[1], category_list[category_index][:-4], card[2]))
    connection.commit()


def main():
    global page, category_index, max_pages

    # walking on products and getting data from all pages
    while category_index != len(category_list):
        max_pages = page = 0
        while page <= max_pages:
            parser()
            page += 1
            sleep(1)
        print('\n\n')
        category_index += 1

# closing database functions
    connection.commit()
    cursor.close()
    connection.close()
    print('Parsing completed! You can close the window if it is not already closed')
    driver.quit()


if __name__ == '__main__':
    main()
