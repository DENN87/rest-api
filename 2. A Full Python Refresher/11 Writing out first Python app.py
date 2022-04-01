"""
1. app will ask user for its age
2. will print how many months that age is equal to
"""

# get user input and convert str to int
user_age = int(input("Enter your age: "))

# calculate total months
months = user_age * 12

# output
print(f"Your age, {user_age} is equal to {months} months.")
