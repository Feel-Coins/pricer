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
dt_list = []
for table in tables:
    if 'onlinetrade_' in table[1]:
        dt_list.append(table[1])
    else:
        pass
for table in tables:
    if 'citilink_' in table[1]:
        dt_list.append(table[1])
    else:
        pass
print(dt_list)

# drop tables


for table in dt_list:
    cursor.execute(f'drop table {table};')
    connection.commit()
# closing all
cursor.close()
connection.close()