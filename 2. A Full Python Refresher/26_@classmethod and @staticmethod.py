"""
Types of class methods
"""

# ---------------- Example 1 ----------------
print("# -- Example 1 --")


class ClassTest:

    # type 1: instance methods
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # type 2:
    @classmethod
    def class_method(cls):  # 'cls' is ClassTest, name of the class top level name
        print(f"Called class_method of {cls}")

    # type 3:
    @staticmethod
    def static_method():
        print(f"Called static_method")


test = ClassTest()

# calling type 1:
test.instance_method()
ClassTest.instance_method(test)

# calling type 2:
ClassTest.class_method()

# calling type 3:
ClassTest.static_method()

# ---------------- Example 2 ----------------
print("# -- Example 2 --")


class Book:
    # variables in class are allowed
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        # creating new objects easily with @classmethod having access to the class or using 'cls'
        # return Book(name, Book.TYPES[0], page_weight + 100)
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        # creating new objects easily with @classmethod having access to the class or using 'cls'
        # return Book(name, Book.TYPES[1], page_weight)
        return cls(name, cls.TYPES[1], page_weight)


# access variable inside a class
print(Book.TYPES)

book_1 = Book("Harry Potter", "hardcover", 1500)
print(book_1)

book_2 = Book.hardcover("Harry Potter", 1500)
print(book_2)

book_3 = Book.paperback("Python Basics", 500)
print(book_3)




