"""
Destructuring variables
"""

# -- Example 1 --
print("\n-- Example 1 --")

x = (5, 11)
print(x, type(x), end = '\n ')

# 'a, b' variable destructuring
a, b = x
print(a, b, sep = ", ")


# -- Example 2 --
print("\n-- Example 2 --")

y = 5, 11, 20, 38
print(y, type(y), end = '\n ')

# destructuring variable 'y'
print(*y, sep = ", ", end = '\n ')

# destructuring only 1st, 2nd variables from 'y'
a, b = x
print(a, b, sep = ", ")


# -- Example 3 --
print("\n-- Example 3 --")

z = [5, 11, 23, 35]
print(z, type(z), end = '\n ')

# destructuring variable 'y'
print(*z, sep = ", ", end = '\n ')

# destructuring only 1st, 2nd variables from 'y'
a, b = x
print(a, b, sep = ", ")


# -- Example 4 --
print("\n-- Example 4 --")

student_attendance = {"Rolf": 96, "Jen": 80, "Adam": 100}

print(type(list(student_attendance.items())), list(student_attendance.items()))
print(student_attendance.items())

for s in student_attendance.items():
    print(s)

# variable destructuring inside 'for' loop
for t, v in student_attendance.items():
    print(f"t= {t}, v= {v}")
    
    
# -- Example 5 --
print("\n-- Example 5 --")
    
people = [
    ("Bob", 42, "Mechanic"),
    ("James", 37, "Artist"),
    ("Anne", 35, "Teacher"),
    ("Rolf", 39, "Farmer"),
    ("Mary", 27, "Student"),
    ]

print(type(people), people)

print("")

# will get error if 'people' list has 2 args but we destructure 3 args
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

print("")
# if we are unsure how many args has our list 'people' this is safer to do
for p in people:
    print(f"Name: {p[0]}, Age: {p[1]}, Profession: {p[2]}")


# -- Example 6 --
print("\n-- Example 6 --")

person = ("Bob", 42, "Mechanic")
# use variable named '_' if you want to skip that upon destructuring
name, _, profession = person
print(name, profession)

# -- Example 7 --
print("\n-- Example 7 --")
# destructuring a list of elements
first, second, *rest, last = [1, 2, 3, 4, 5, {"name": "Bob"}]
# '*rest' is collecting all the destructuring values
# after 'first' and 'second' into one single variable
# 'last' will get the very last item from the list[]
print(first, type(first))
print(second, type(second))
print(rest, type(rest))
print(last, type(last))





