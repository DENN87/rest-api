"""
Exercise Classes

    1. The '__init__'  method, which should take an argument, 'name'. It should initialise 'self.name'
to be the argument, and 'self.items' to be an empty list.

    2. The 'add_item'  method, which should append a dictionary representing an item to the store's 'items'
property. The dictionary should have keys 'name' and 'price'.

    3. The 'stock_price'  method, which should add up each item price inside 'self.items' to come up
with a total, and return that.
"""


# initial code
# class Store:
#     def __init__(self):
#         pass
#
#     def add_item(self, name, price):
#         pass
#
#     def stock_price(self):
#         pass


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        return sum(item['price'] for item in self.items)
