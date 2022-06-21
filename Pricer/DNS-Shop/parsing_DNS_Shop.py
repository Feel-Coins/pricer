# scraper for DNS-shop
import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent

def get_data():
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
         'User-Agent' : ua.random
    }

    cookies ={
        '_ym_d': '1650375664',
        '_ym_uid': '1650375664651647118',
        'city_path': 'novosibirsk',
        'lang': 'ru',
        'PHPSESSID':'5941929e9a99389592775e2a9c1be6d6',
        'current_path': '496e8c1db6d13234d11129c25618dd41a1e573a9d7e11823c587bd344e9d852ca%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A142%3A%22%7B%22city%22%3A%2258b139d1-90ae-11dc-a1f0-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041d5Cu043e%5Cu0432%5Cu043e%5Cu0441%5Cu0438%5Cu0431%5Cu0438%5Cu0440%5Cu0441%5Cu043a%22%2C%22method%22%3A%22url%22%7D%22%3B%7D',
        '_csrf': '9d6b3441c9bda177f0b2e70a103aa0847c7bde90b4332d52c22d1942a28ca20a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22TL75IMtgbRZ1rw6JGD5tuLZyyNZktG5q%22%3B%7D',
        'phonesIdent': '06f871f2e4eb9d85aebb2f812c8e72fa60ce750b6150d49ba99be0ed506e67daa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22a4c48657-0cf2-4ed2-b6f7-77d7b21244f3%22%3B%7D',
        'rerf': 'AAAAAGKxL7NWwV/wNTQUAg==',
        'ipp_uid': '1655779251359/GE964hjar3WGorbY/1UHN9H71vmetqnqWTI1jrw==',
        '_ga': 'GA1.2.126023277.1655779257',
        '_gid': 'GA1.2.317343255.1655779257',
        '_gcl_au': '1.1.724438015.1655779257',
        '_gaexp': 'GAX1.2.F5r0LoWFQuaGkKl-pfLADg.19228.0',
        '_ym_isad': '2',
        'cartUserCookieIdent_v3': '5d5f71a1b3f3fca8f6c59a69fdb06da90e6dcb44d73c7e830c9516d733a1392ea % 3A2 % 3A % 7Bi % 3A0 % 3Bs % 3A22 % 3A % 22cartUserCookieIdent_v3 % 22 % 3Bi % 3A1 % 3Bs % 3A36 % 3A % 22a9daa645 - 400f - 3bf6 - 8b5e - 3b3c3ca0ee55 % 22 % 3B % 7D',
        'rsu - configuration - id': '61b7f318a297380ea626cdf3f7746ed10cbceb1b7d9bc4d59300855a94345019a % 3A2 % 3A % 7Bi % 3A0 % 3Bs % 3A20 % 3A % 22rsu - configuration - id % 22 % 3Bi % 3A1 % 3Bs % 3A36 % 3A % 2200129caa - 1a83 - 46e0 - 943b - 677d8a6a7980 % 22 % 3B % 7D',
        'ipp_key': 'v1655800354616/v33947245ba5adc7a72e273/ASYXeHDgOfsgBmWEJXDVMQ==',
        '_ym_visorc': 'b',
        'dnsauth_csrf': '3bab7568a8321a7203c6fcacf64bc63d726a8ca21d1b632690a22efc86fa001aa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%2254699c20-94d9-4159-87fa-21b663b3109a%22%3B%7D',
        '_gat': '1'
    }
    response = requests.get(url='https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/', headers=headers, cookies=cookies)

    with open('data.json', 'w') as file:
        file.write(response.text)

def main():
    get_data()


if __name__ == '__main__':
    main()
