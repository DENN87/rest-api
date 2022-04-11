"""
Dictionary comprehensions
"""

# -- Example 1 --
print("# -- Example 1 --")


users = [
    (0, "Anne", "password"),
    (1, "Bob", "bob123"),
    (2, "Rolf", "long4password"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(username_mapping["Rolf"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# destructuring
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")
