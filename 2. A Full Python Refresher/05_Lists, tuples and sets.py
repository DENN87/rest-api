"""
Lists, tuples and sets
"""

l = ["Bob", "Rolf", "Anne"]

t = ("Bob", "Rolf", "Anne")

s = {"Bob", "Rolf", "Anne"}

print(l[0])
print(t[0])
# 'set' object is not subscriptable
# print(s[0])
print(s)

l[1] = "Smith"
print(l)

# 'tuple' object does not support item assignment
# t[1] = "Smith"

# 'set' object does not support item assignment
# s[0] = "Smith"

l.append("John")
print(l)

l.remove("Bob")
print(l)

# 'tuple' object can't add or remove element

s.add("Ayla")
# duplicates are not allowed in 'set' object
s.add("Ayla")
print(s)

s.remove("Bob")
print(s)
