import sqlite3 as sl
from faker import Faker
from time import time

f = Faker()

connection = sl.connect("fake-data.db")

cursor = connection.cursor()

for i in range(100):
    query = f"insert into people (name, email) values"
    cursor.execute(query)

connection.commit()
connection.close()

end = time()

print(end - start)