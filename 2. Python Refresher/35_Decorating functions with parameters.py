"""
Decorating functions with parameters
"""


# ---------------- Example 1 ----------------
import functools


user = {"username": "jose", "access_level": "admin"}


# 'make_secure' is a decorator function for 'get_admin_password'
def make_secure(func):
    @functools.wraps(func)  # to keep the 'get_admin_password' function name, otherwise 'secure_function'
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password("billing"))
print(get_password.__name__)
