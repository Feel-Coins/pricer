import psycopg2

# connecting to the DB
connection = psycopg2.connect('dbname=Pricer user=postgres')
cursor = connection.cursor()

# exec all table info
cursor.execute("SELECT * FROM pg_catalog.pg_tables")
tables = cursor.fetchall()
tables.sort()

# shop list
shops = ['citilink_', 'onlinetrade_']

# searching all shop tables
dt_list_citilink = []
dt_list_onlinetrade = []
for table in tables:
    if f'{shops[0]}' in table[1]:
        dt_list_citilink.append(table[1])
    elif f'{shops[1]}' in table[1]:
        dt_list_onlinetrade.append(table[1])
    else:
        pass

latest_dt = [max(dt_list_citilink), max(dt_list_onlinetrade)]
print(f'founded dt: {latest_dt}\n')


# searching by product_name
def searching(prod):
    for i in latest_dt:
        cursor.execute(f'SELECT product_name, price, link FROM {i} WHERE UPPER (Product_name) LIKE '
                       f'UPPER (\'%{prod}%\') ORDER BY price ASC;')
        request = f'SELECT product_name, price, link FROM {i} WHERE UPPER (Product_name) LIKE '\
                  f'UPPER (\'%{prod}%\') ORDER BY price ASC;'
        print(request)

        for data in cursor.fetchall():
            print("\nname =", data[0], )
            print("price =", data[1])
            print("link =", data[2])


searching(prod=str(input('please input searching product name (example: RTX3050 / i5 11400): ')))


# closing all
cursor.close()
connection.close()
