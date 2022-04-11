"""
Functions in Python
"""


# -- Example 1 --
print("# -- Example 1 --")
def hello(name):
    print(f"Hello, {name}!")


hello("Denis")


# -- Example 2 --
print("# -- Example 2 --")
def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


print("Welcome to the page in seconds program!")

user_age_in_seconds()

print("GoodBye!")


# -- Example 3 --
print("# -- Example 3 --")
friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name]
    return f


print(add_friend())


# -- Example 4 --
print("# -- Example 4 --")

friends = []

def add_friend():
    friends.append("Jane")
    

add_friend()

print(friends)






