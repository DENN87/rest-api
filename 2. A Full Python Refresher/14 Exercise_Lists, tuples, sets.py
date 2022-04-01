"""
1. Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
2. Create a tuple, called my_tuple, with a single value in it.
3. Modify the variable set2 = {5} so that set1.intersection(set2) returns {5, 77, 9, 12}
"""

# 1
my_list = [4, 15, 81]

# 2
my_tuple = (11,)

# 3
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

inter = set1.intersection(set2)
print(inter)
