import psycopg2
import psycopg2.extras

HOSTNAME = '127.0.0.1'
USERNAME = 'postgres'
PASSWORD = 'jon123'
DATABASE = 'public'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

cursor = connection.cursor()

query = "SELECT * FROM items;"

cursor.execute(query)

results = cursor.fetchall()

connection.close()

for i in results:
    print(i)

# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)