import psycopg2

#searching latest citilink table in DB
connection = psycopg2.connect('dbname=Pricer user=postgres')
cursor = connection.cursor()
cursor.execute("SELECT * FROM pg_catalog.pg_tables")
rows = cursor.fetchall()
rows.sort()
dt_list = []
for row in rows:
    if 'citilink_' in row[1]:
        dt_list.append(row[1])
    else:
        pass

latest_dt = max(dt_list)
print(f'connected to {latest_dt}\n')


#searching by product_name
def searching(prod):
    cursor.execute(f'SELECT product_name, price, link FROM {latest_dt} WHERE UPPER (Product_name) LIKE '
                   f'UPPER (\'%{prod}%\') ORDER BY price ASC;')
    request = f'SELECT product_name, price, link FROM {latest_dt} WHERE UPPER (Product_name) LIKE '\
              f'UPPER (\'%{prod}%\') ORDER BY price ASC;'
    print(request)

    for data in cursor.fetchall():
        print("\nname =", data[0], )
        print("price =", data[1])
        print("link =", data[2])


searching(prod=str(input('please input searching product name (example: RTX3050 / i5 11400): ')))


#closing all
cursor.close()
connection.close()
