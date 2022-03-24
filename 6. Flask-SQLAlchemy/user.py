import sqlite3

from flask_restful import Resource, reqparse


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


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = "This field cannot be blank."
                        )
    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = "This field cannot be blank."
                        )
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password'],))
        
        connection.commit()
        connection.close()
        
        return {"message": "User created successfully."}, 201

# TO IMPLEMENT FOR ADMIN USER ONLY
# from flask_jwt import jwt_required, current_identity
# class User(Resource):
#     @jwt_required()
#     def get(self):   # view all users
#         user = current_identity
#         # then implement admin auth method
