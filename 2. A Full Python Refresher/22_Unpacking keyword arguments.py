"""
Unpacking keyword arguments
"""

# -- Example 1 --
print("# -- Example 1 --")

def named(**kwargs):  # keyword arguments get collected in 'kwargs'
    print(kwargs)


named(name="Bob", age=25)  # 'name' and 'age' are arguments


# -- Example 2 --
print("# -- Example 2 --")

def named_v2(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named_v2(*details)  # returns 'name age'
named_v2(**details)  # returns 'Bob 25'


# -- Example 3 --
print("# -- Example 3 --")

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# -- Example 4 --
print("# -- Example 4 --")

def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)


# -- Example 5 --
print("# -- Example 5 --")

def myfunction(**kwargs):
    print(kwargs)


myfunction(**{"Bob": 25, "Anne": 22})  # correct
myfunction(**"Bob")  # Error, must be mapping
myfunction(**None)  # Error
