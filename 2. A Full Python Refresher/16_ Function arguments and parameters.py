"""
Function arguments and parameters
"""

# -- Example 1 --
print("# -- Example 1 --")


def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")


add(5, 3)


# -- Example 2 --
print("# -- Example 2 --")


def say_hello(firstname, lastname):
    print(f"Hello, {firstname} {lastname}")


say_hello("Bob", "Smith")
say_hello(lastname="Bob", firstname="Smith")


# -- Example 3 --
print("# -- Example 3 --")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("Can't divide by 0!")


divide(dividend=15, divisor=2)
divide(dividend=15, divisor=0)
