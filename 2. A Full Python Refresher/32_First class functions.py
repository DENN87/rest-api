"""
First class functions - means functions are just variables and can be passed in as
arguments and use them just like a variable.
"""


# ---------------- Example 1 ----------------
print("# -- Example 1 --")

def divide(dividend: int, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)  # passing divide as an argument to another function
print(result)


# ---------------- Example 2 ----------------
print("# -- Example 2 --")

from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 28},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", itemgetter("name")))
print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Bob Smith", get_friend_name))
