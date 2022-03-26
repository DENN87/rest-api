import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

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
        
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400
        
        user = UserModel(data['username'], data['password'])  # (**data) unpacking data
        user.save_to_db()
        
        return {"message": "User created successfully."}, 201

# TO IMPLEMENT FOR ADMIN USER ONLY
# from flask_jwt import jwt_required, current_identity
# class User(Resource):
#     @jwt_required()
#     def get(self):   # view all users
#         user = current_identity
#         # then implement admin auth method
