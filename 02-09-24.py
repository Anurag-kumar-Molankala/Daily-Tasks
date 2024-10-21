# Tuple:- A tuple can be created using parentheses () or the tuple() function.

#Creating an Empty Tuple
empty_tuple = ()
empty_tuple2 = tuple()

print(empty_tuple)  # Output: ()
print(empty_tuple2) # Output: ()

print("-----")

# Unpacking a Tuple into Variables - Unpacking a tuple means assigning its elements to multiple variables.
my_tuple = (10, 20, 30)
a, b, c = my_tuple

print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

print("-----")

# Adding an Item to a Tuple - Tuples are immutable, meaning their contents cannot be changed directly. However, you can add an item by converting the tuple to a list, adding the item, and converting it back to a tuple.
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)

print(my_tuple)  # Output: (1, 2, 3, 4)

print("-----")

# Converting a Tuple into a String - You can convert a tuple into a string by using the join() method.
my_tuple = ('a', 'b', 'c')
my_string = ''.join(my_tuple)

print(my_string)  # Output: 'abc'

print("-----")

# Finding the Most Frequent Element in a Tuple - You can use the max() function with the key argument set to tuple.count to find the most frequent element.
my_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
most_frequent = max(my_tuple, key=my_tuple.count)

print(most_frequent)  # Output: 4

print("-----")

# Concatenation of Tuples - You can concatenate tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2

print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

print("-----")

# Repetition of Tuples - You can repeat tuples using the * operator.
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 2

print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

print("-----")

# Nesting of Tuples - A tuple can contain other tuples as elements, creating a nested tuple.
nested_tuple = (1, 2, (3, 4), 5)

print(nested_tuple)  # Output: (1, 2, (3, 4), 5)

print("-----")

# Slicing of Tuples - You can slice a tuple using the : operator.
my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]

print(sliced_tuple)  # Output: (2, 3, 4)

print("-----")

# Removing Elements from a Tuple - Since tuples are immutable, you cannot directly remove elements. But you can create a new tuple without the unwanted elements.
my_tuple = (1, 2, 3, 4)
my_tuple = tuple(x for x in my_tuple if x != 3)

print(my_tuple)  # Output: (1, 2, 4)

print("-----")

# Type Casting - Type casting is converting one data type into another. For example, converting a tuple into a list or a string.
my_tuple = (1, 2, 3)
my_list = list(my_tuple)

print(my_list)  # Output: [1, 2, 3]

print("-----")

# For Loop in Tuple - You can iterate through a tuple using a for loop.
my_tuple = (10, 20, 30)
for item in my_tuple:
    print(item)

print("-----")

print("End of the Day 9 Session")