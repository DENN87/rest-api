"""
Dictionaries
"""
# Example 1:
print("\n-- Example 1 --")
friend_ages = {"Rolf": 24, "Jen": 26, "Adam": 23}

print(friend_ages.values())
print(friend_ages.items())
print(f'Adam is {friend_ages.get("Adam")}')
print(friend_ages.popitem())
print(friend_ages.__contains__("Jen"))

friend_ages["Adam"] = 30
print(f'Adam is {friend_ages["Adam"]}')

friend_ages["Bob"] = 21
friend_ages["Zelda"] = 25
print(friend_ages)


# Example 2:
print("\n-- Example 2 --")
friends = []

for f in friend_ages.items():
    item = {"name": f[0], "age": f[1]}
    friends.append(item)
print(f"Friends 'for' loop: \n{friends}")

# list comprehension for Example 2
f_list = [{"name": f[0], "age": f[1]} for f in friend_ages.items()]
print("Friends List Comp:\n", f_list)


# Example 3:
print("\n-- Example 3 --")
student_attendance = {"Rolf": 96, "Jen": 80, "Adam": 100}

for student in student_attendance:
    print(student, ": ", student_attendance[student])

print("")

for student, attendance in student_attendance.items():
    print(student, ": ", attendance)

# this if statement is not checking
if "Jen" in student_attendance:
    print(f"Jen: {student_attendance['Jen']}")
else:
    print("Jen is not a student in this class.")

print("")

attendance_values = student_attendance.values()
print(f"Attendance average: {sum(attendance_values) / len(attendance_values)}")



