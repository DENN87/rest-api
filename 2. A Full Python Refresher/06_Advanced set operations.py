"""
Advanced set operations
"""

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# Report whether this set contains another set.
superset = friends.issuperset(abroad)
print(superset)
superset = abroad.issuperset(friends)
print(superset)

# Return the difference of two or more sets as a new set.
local_friends = friends.difference(abroad)
print(local_friends)

# Return the union of sets as a new set.
all_friends = friends.union(abroad)
print(all_friends)


art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# Return the intersection of two sets as a new set.
both = art.intersection(science)
print(both)

# Return the symmetric difference of two sets as a new set.
diff = art.symmetric_difference(science)
print(diff)


