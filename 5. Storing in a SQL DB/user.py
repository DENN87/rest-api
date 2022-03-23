import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id,
        self.username = username,
        self.password = password

    # retrieve user object by username
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  # always a tuple with 2nd arg missing (arg1,)
        # getting the first row
        row = result.fetchone()
        # if there is a row
        if row:
            # creating a new User object with the data from row
            user = cls(*row)  # *row = row[0], row[1], row[2] = columns id, username, password
        else:
            user = None
            
        connection.close()
        return user
    
    # retrieve user object by id
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
            
        connection.close()
        return user
    