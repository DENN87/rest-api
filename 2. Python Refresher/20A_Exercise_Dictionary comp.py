"""
Exercise Dictionary comprehensions

# Create a dictionary variable, called 'student'
# Modify a variable, 'grades', so it contains the value of a dictionary's key
# Implement a function calculating a total average grade for a class of students
"""


# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88
student = {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
}

# Assume the argument, data, is a dictionary
# Modify the grades variable, so it accesses the 'grades' key of the data dictionary
def average_grade(data):
    # Implement here
    grades = student['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for s in student_list:
        # Implement here
        total += sum(s['grades'])
        count += len(s['grades'])

    return total / count


