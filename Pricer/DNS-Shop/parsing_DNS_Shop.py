# scraper for DNS-shop
import requests
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

    with open('data.json', 'w') as file:
        file.write(response.text)

    with open('data.json') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='ProductCardHorizontal__title')

    for card in cards:
        card_title = card.text.strip()

    with open('titles.json', 'w') as file:
        file.write(card_title.text)



def main():
    get_data()


if __name__ == '__main__':
    main()
