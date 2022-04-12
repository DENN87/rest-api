"""
Simple decorator function
"""


# ---------------- Example 1 ----------------

def get_admin_password():
    return "1234"

# 'make_secure' is a decorator function for 'get_admin_password'
def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


user = {"username": "jose", "access_level": "guest"}

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())