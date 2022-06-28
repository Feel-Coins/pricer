import json
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

Shop = 'Mvideo'
Site = 'https://www.mvideo.ru/komputernye-komplektuushhie-5427/videokarty-5429'
Cards_teg = 'a'
Cards_class = 'product-title__text'
Prices_teg = 'span'
Prices_class = 'price__main-value'


def get_data_selen():
    #open browser
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    browser = webdriver.Chrome(options=options)
    #clear all cash and cookies
    browser.get('chrome://settings/clearBrowserData')
    sleep(3)
    actions = ActionChains(browser)
    actions.send_keys(Keys.TAB * 7 + Keys.ENTER)
    actions.perform()
    sleep(1.5)
    #get html
    browser.get(url=Site)
    generated_html = browser.page_source
    sleep(3)
    browser.quit()

    with open(f'data from {Shop}.json', 'w') as file:
        file.write(generated_html)


def work_with_data():

    with open(f'data from {Shop}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all(teg=Cards_teg, class_=Cards_class)
    prices = soup.find_all(teg=Prices_teg, class_=Prices_class)


if __name__ == '__main__':
    get_data_selen()
    # work_with_data()
