"""
Errors in Python
"""


def divide(dividend: int, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


# ---------------- Example 1 ----------------
print("# -- Example 1 --")

grades = []

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as error:
    # print(error)
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}")

finally:
    print("Thank You!")


# ---------------- Example 2 ----------------
print("# -- Example 2 --")

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [85, 95]},
]

try:  # Try to run this
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:  # run this if error is True
    print(f"Error: {name} has no grades!")
else:  # run this if no error
    print("-- All student averages calculated --")
finally:  # run this no matter what
    print("-- End of student average calculation --")

