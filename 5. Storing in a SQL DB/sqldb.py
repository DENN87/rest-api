import sqlite3

# initialize a connection to DB file
connection = sqlite3.connect('data.db')

# setting a cursor to execute the queries and stores the result for access
cursor = connection.cursor()

# creating a table query in SQL
create_table = "CREATE TABLE users (id int, username text, password text)"
# executing the query
cursor.execute(create_table)

# creating a user (tuple)
user = (1, 'Test', 'asdf')

# a query to insert a user with its values
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# executing the query
cursor.execute(insert_query, user)

# creating multiple users values
users = [
    (2, 'Test 2', 'asdf'),
    (3, 'Test 3', 'asdf'),
    (4, 'Test 4', 'asdf')
]

# executing the query for many users
cursor.executemany(insert_query, users)

# retrieve data from SQL DB (* - select all)
select_query = "SELECT * FROM users"
# executing the query
for row in cursor.execute(select_query):
    print(row)

# saving the changes to SQL DB file
connection.commit()

# closing the connection to SQL DB
connection.close()
