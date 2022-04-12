"""
Booleans in Python
"""

print(5 == 5)
print(5 < 5)
print(10 != 10)

# Comparisons: ==, !=, >, <, >=, <=

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)
print(friends is abroad)

# 'is' compares if it is the same thing, not just the elements

friends = ["Rolf", "Bob"]
abroad = friends

print(friends == abroad)
print(friends is abroad)
