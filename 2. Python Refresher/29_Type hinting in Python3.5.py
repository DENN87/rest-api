"""
Type hinting in Python 3.5
"""
from typing import List

# '->' return type float
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


list_avg(123)


# type hint class Book 'name: str, page_count: int'
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count


# type hint class BookShelf 'books: List[Book]'
class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    # '->' return type str
    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


# type hint class Book
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":  # return Book object, same class "Book", other class type - without quotes
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":  # return Book object
        return cls(name, cls.TYPES[1], page_weight)



