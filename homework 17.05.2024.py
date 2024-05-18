import psycopg2
import requests

url = f'https://dummyjson.com/users/'
r = requests.get(url)

db_name = 'new_db'
password = '123'
host = 'localhost'
port = 5432
user = 'postgres'

conn = psycopg2.connect(dbname=db_name,
                        user=user,
                        password=password,
                        host=host,
                        port=port)



create_table_products_query = """create table products(
        id serial primary key ,
        first_name varchar(255) ,
        last_name varchar (155) ,
        maiden_name varchar(255),
        age int,
        email varchar (255) ,
        phone varchar (255)
);"""

cur = conn.cursor()

insert_into_query = """insert into products (first_name, last_name, maiden_name, age, email, phone)

    values (%s,%s,%s,%s,%s,%s);

"""

for user in r.json()['users']:
    cur.execute(insert_into_query, (
        user['first_name'], user['last_name'], user['maiden_name'], user['age'], user['email'],
        user['phone']))
    conn.commit()