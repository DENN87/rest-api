"""
Strings in Python
"""
name = "Bob"
print(f"Hello, {name}")

name = "Rolf"
print(f"Hello, {name}")

# template strings
name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

# longer templates
longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")

print(formatted)
