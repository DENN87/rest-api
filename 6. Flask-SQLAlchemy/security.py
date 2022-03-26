from werkzeug.security import safe_str_cmp
from models.user import UserModel
from hmac import compare_digest

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user
safe_str_cmp()

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
