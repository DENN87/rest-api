from werkzeug.security import safe_str_cmp

from user import User

users = [
    User(1, 'First', 'pass'),
    User(2, 'Second', 'pass'),

]

username_mapping = {u.username[0]: u for u in users}

userid_mapping = {u.id[0]: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id[0], None)
