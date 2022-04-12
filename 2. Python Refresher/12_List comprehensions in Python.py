"""
List comprehension in Python
"""

# Example 1
numbers = [1, 3, 5]

doubled_comp = [x * 2 for x in numbers]

doubled_for = []

for n in numbers:
    doubled_for.append(n * 2)
    
print(f"List comp: {doubled_comp}")
print(f"'for' loop: {doubled_for}")

# Example 2
friends = ["Rolf", "Sam", "Samantha", "Sarah", "Jen"]
starts_s_comp = [f for f in friends if f.startswith("S")]
starts_s_for = []

for f in friends:
    if f.startswith("S"):
        starts_s_for.append(f)
    
print(f"List comp: {starts_s_comp}")
print(f"'for' loop: {starts_s_for }")

print(starts_s_comp is starts_s_for)
print(type(starts_s_comp), type(starts_s_for))
print(id(starts_s_comp), id(starts_s_for))
