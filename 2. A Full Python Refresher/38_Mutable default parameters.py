"""
Mutable default parameters
"""

from typing import List, Optional


# Bad Practice:
# def __init__(self, name: str, grades: List[int] = []):  # This is bad, assign an empty list
# this will be initialized when the class Student was created NOT WHEN CALLED

class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad! NO MUTABLE DEFAULT PARAMETERS SHOULD BE USED
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


# both students 'bob' and 'rolf' are sharing the same List[int] = []
bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)


# Correct Practice:
# def __init__(self, name: str, grades: Optional[List[int]] = None):  # This is better!
# self.grades = grades or []
# this way each student will have its own grades list
