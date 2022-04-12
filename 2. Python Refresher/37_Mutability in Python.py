"""
Mutability in Python - changing a list after it was created means a list is mutable
"""

# list - mutable
a = []
b = a
c = []

a.append(35)

print(id(a))
print(id(b))
print(id(c), '\n')

print(a)
print(b)
print(c, '\n')


# tuple - immutable
a = ()
b = ()

a = a + (15, )  # this will create a new tuple, not modify the first 'a = []' tuple

print(id(a))
print(id(b), '\n')


# integer - immutable

a = 8597
b = 8597

# same memory location for equal integer variable with the same value integer
print(id(a))
print(id(b), '\n')

a = 9251

print(id(a))
print(id(b), '\n')


# string - immutable

a = "Hello"
b = a

print(id(a))
print(id(b), '\n')

a += "world"  # not changing the string "Hello" but changing variable 'a'

print(id(a))
print(id(b), '\n')

