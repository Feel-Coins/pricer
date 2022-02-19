#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99}
    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99}
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99}
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price2': 59.99},
        {'shop': 'магнит', 'price3': 62.99}
    ]
}
sweets_list = sweets.get('пирожное')
print(sweets_list)
# [{'shop': 'ашан', 'price': 67.99}, {'shop': 'пятерочка', 'price2': 59.99}, {'shop': 'магнит', 'price3': 62.99}]


# Пирожные
pie_auchan = list(sweets_list[0].values())
pie_5 = list(sweets_list[1].values())
pie_magnet = list(sweets_list[2].values())

print('пирожные:', pie_5, pie_magnet, pie_auchan, '\n')

# Указать надо только по 2 магазина с минимальными ценами

#                       ПОПРОБУЙ СДЕЛАТЬ НА ПРИМЕРЕ ЗАДАНИЯ 10!!!

shops_auchan = shops['ашан']
auchan_values = [list(shops_auchan[0].values()), list(shops_auchan[1].values()), list(shops_auchan[2].values())]
print(auchan_values)

shops_pyatorochka = shops['пятерочка']
pyatorochka_values = [
    list(shops_pyatorochka[0].values()),\
    list(shops_pyatorochka[1].values()),\
    list(shops_pyatorochka[2].values())
    ]
print(pyatorochka_values)

shops_magnet = shops['магнит']
magnet_values = [
    list(shops_magnet[0].values()),\
    list(shops_magnet[1].values()),\
    list(shops_magnet[2].values())
    ]
print(magnet_values)

#ПРОВЕРКА
