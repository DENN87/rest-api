"""
Default parameter values
"""


# -- Example 1 --
print("# -- Example 1 --")

def add(x, y=8):
    result = x + y
    print(f"{x} + {y} = {result}")


add(5, )
add(x=5, )


# -- Example 2 --
print("# -- Example 2 --")

default_y = 3

def add(x, y=default_y):
    result = x + y
    print(f"{x} + {y} = {result}")


add(2)

default_y = 4
add(2)
