"""
Unpacking arguments
"""


# -- Example 1 --
print("# -- Example 1 --")

def multiply(*args):  # *args - a set of arguments
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 3, 5))


# -- Example 2 --
print("# -- Example 2 --")

def add(x, y):
    return x + y


nums = [3, 5]
add(*nums)  # destructuring nums
print(add(*nums))

nums_dict = {"x": 15, "y": 5}
print(add(nums_dict["x"], nums_dict["y"]))  # similarly '*nums_dict.values()'
print(add(*nums_dict.values()))  # similarly '**nums_dict'
print(add(**nums_dict))  # similarly '**nums_dict'


# -- Example 3 --
print("# -- Example 3 --")

def apply(*args, operator):
    if operator == "*":
        # return multiply(args)  # wrong, list of list
        return multiply(*args)  # correct arguments of the list
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="*"))
