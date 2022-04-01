"""
User Input in Python
"""
name = input("Enter your name: ")
print(name)

# input always returns a string

size_input = input("How big is your house (in sq.ft.): ")
square_meters = int(size_input) / 10.76391041671
print(f"Bob, your house of {size_input} square feet is approximately {square_meters:.2f} square meters.")




