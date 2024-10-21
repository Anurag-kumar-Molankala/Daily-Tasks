""" Set: A set in Python is a collection that can store multiple values in a single variable. Here are some key characteristics of a set:

Unordered: The items in a set do not have a defined order.
Unchangeable: Once you add an item to a set, you cannot change it, but you can add or remove items.
Duplicates Not Allowed: A set cannot have two items with the same value. """

# How to create set: You can create a set by placing your items inside curly braces {} or by using the set() function.
my_set = {1, 2, 3, 4}
print(my_set) # This creates a set called my_set with the values 1, 2, 3, and 4.

print("-----")

# Removing Items from a Set:
# remove(): This method removes a specific item from the set. If the item is not found, it will cause an error.
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set) # Now, my_set is {1, 2, 4}

print("-----")

# descard() - This method also removes a specific item from the set. However, if the item is not found, it will not cause an error.
my_set = {1, 2, 3, 4}
my_set.discard(3)
print(my_set) # Now, my_set is {1, 2, 4}

print("-----")

# clear() - This method removes all items from the set, leaving it empty.
my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set) # Now, my_set is set() or an empty set

print("-----")

# del() - This deletes the entire set.
my_set = {1, 2, 3, 4}
del my_set # Now, my_set is deleted and no longer exists

print("-----")

# pop() - This method removes a random item from the set because sets are unordered. You don't know which item will be removed.
my_set = {1, 2, 3, 4}
my_set.pop()
print(my_set) # Now, my_set is {2, 3, 4} or another set missing one random element

print("-----")

# Mathematical Operations with Sets:

# Union - Combines all items from two or more sets, without duplicates.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set) # union_set is {1, 2, 3, 4, 5}

print("-----")

# Intersection - Finds the common items between two or more sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set) # intersection_set is {3}

print("-----")

# Difference - Finds the items that are in the first set but not in the second.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set) # difference_set is {1, 2}

print("-----")

# Symmetric Difference - Finds items that are in either of the sets but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) # symmetric_difference_set is {1, 2, 4, 5}

print("-----")

print("End of the Day 10 Session")