"""
Magic methods_ __str__ and __repr__
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # magic method '__str__' gets called when you want to turn your object
    # into a 'str' string representation
    def __str__(self):  # by default gets called
        return "Hello, " + self.name

    # return a string that allows to recreate the initial object easily
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)
print(bob)  # printing 'bob' object, python automatically calls 'bob.__str__()'
print(bob.__str__())  # similarly 'print(bob)'
print(bob.__repr__())

