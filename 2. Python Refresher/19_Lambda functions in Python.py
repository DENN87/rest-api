"""
Lambda functions in Python
"""

# -- Example 1 --
print("# -- Example 1 --")


def add(x, y):
    return x + y


print(add(5, 8))

# with lambda
add = lambda x, y: x + y  # wrong, not best practices
print(add(2, 2))

# -- Example 2 --
print("# -- Example 2 --")


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [x * 2 for x in sequence]
doubled_list_comp = [double(x) for x in sequence]  # faster
doubled_map = list(map(double, sequence))
# 'map' returns a map object, and it should be converted to a list

# lambda used in 'map' for readability
doubled_map_lambda = list(map(lambda x: x * 2, sequence))
# 'map' returns a map object, and it should be converted to a list

print(doubled)
print(doubled_list_comp)
print(doubled_map)
print(doubled_map_lambda)
