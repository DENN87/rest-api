import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# id INTEGER PRIMARY KEY - will be assigned automatically by DB and autoincrement for every new user created
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES ('new-item', 10.99)")

connection.commit()

connection.close()
