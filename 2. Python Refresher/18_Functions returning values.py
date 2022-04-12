"""
Functions returning values
"""

# -- Example 1 --
print("# -- Example 1 --")

def add(x, y):
    print(x + y)


add(5, 8)
result = add(5, 8)
print(result)

# correct
def add(x, y):
    return x + y


result = add(5, 8)
print(result)


# -- Example 2 --
print("# -- Example 2 --")

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "Can't divide by 0!"


result = divide(dividend=15, divisor=2)
print(result)

result = divide(dividend=15, divisor=0)
print(result)


