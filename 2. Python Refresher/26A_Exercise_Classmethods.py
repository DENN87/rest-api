"""
Exercise ClassMethods

This coding exercise requires you to complete two method implementations.
    1. The 'franchise'  method, which takes in a store as argument. It should return a
    new 'Store' object, with a name equal to the argument + " - franchise".
    2. The 'store_details'  method, which also takes in a store as argument. It should
    return a string representing the argument.

A few examples:
    store = Store("Test")
    store2 = Store("Amazon")
    store2.add_item("Keyboard", 160)

    Store.franchise(store)  # returns a Store with name "Test - franchise"
    Store.franchise(store2)  # returns a Store with name "Amazon - franchise"

    Store.store_details(store)  # returns "Test, total stock price: 0"
    Store.store_details(store2)  # returns "Amazon, total stock price: 160"

When completing the 'store_details'  method, you may need to convert the output of 'store.stock_price'
to an integer. You can do this like so: int(store.stock_price).

"""

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return f"{self.name}"

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        return sum(item['price'] for item in self.items)

    @classmethod
    def franchise(cls, store):
        # returns a New Store with the given 'name' + 'str'
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {int(store.stock_price())}"


store = Store("Test")
store.add_item("Mouse", 10)

store2 = Store("Amazon")
store2.add_item("Keyboard", 160)


print(Store.franchise(store))  # Test - franchise
print(Store.franchise(store2))  # Amazon - franchise
print(Store.store_details(store))  # Test, total stock price: 10
print(Store.store_details(store2))  # Amazon, total stock price: 160
