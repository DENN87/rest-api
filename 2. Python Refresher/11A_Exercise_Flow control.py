"""
1. Modify the code so that the 'evens' list contains only the even numbers of the 'numbers'
    list. You do not need to print anything.
2. Add a clause to the if statement such that if the user's input is "q", the program
    prints "Quit".
Attn: Careful with upper and lowercase letters.
"""

# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
odds = []
for number in numbers:
    # even numbers number % 2 == 0
    if number % 2 == 0:
        evens.append(number)
    # odd numbers number % 2 == 1
    else:
        odds.append(number)

print(f"Even Numbers: {evens}")
print(f"Odd Numbers: {odds}")


# -- Part 2 --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input in ("q", "Q"):
    print("Quit")


