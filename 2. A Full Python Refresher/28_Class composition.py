"""
class composition - is a counterpart to inheritance to build out classes that use other classes
"""

class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book_1 = Book("Harry Potter")
book_2 = Book("Python Basics")

shelf = Bookshelf(book_1, book_2)

print(shelf)

print(shelf.books)  # returns tuple of Book objects
print(book_1)
