"""
Object Oriented Programming
"""


# -- Example 1 --
print("# -- Example 1 --")

student_1 = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student_1['grades']))


# -- Example 2 OOP --
print("# -- Example 2 OOP --")

# Define a class
class Student:
    def __init__(self):  # 'self' is an empty object
        self.name = "Rolf"  # accessing a 'name' property inside 'self'
        self.grades = (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)


# use the class 'Student' to create '()' a new thing called 'self' <object>
student_2 = Student()

# accessing 'name' property
print(student_2.name)

# accessing 'grades' property
print(student_2.grades)

# accessing 'average()' method
print(student_2.average())
print(Student.average(student_2))


# -- Example 3 OOP --
print("# -- Example 3 OOP --")

# Define a class
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student_3 = Student("Jane", (94, 96, 98, 100))

print(student_3.name)
print(student_3.grades)
print(student_3.average_grade())
print(Student.average_grade(student_3))
