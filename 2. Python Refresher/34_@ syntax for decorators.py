"""
@ syntax for decorators
"""


# ---------------- Example 1 ----------------
import functools

# 'make_secure' is a decorator function for 'get_admin_password'
def make_secure(func):
    @functools.wraps(func)  # to keep the 'get_admin_password' function name, otherwise 'secure_function'
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

@make_secure
def get_admin_password():
    return "1234"


user = {"username": "jose", "access_level": "admin"}

print(get_admin_password())
print(get_admin_password.__name__)
