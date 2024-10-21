# 1.Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
# Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)

nested_tuple = (1, (2, 3), (4, 5), 6)
x = str(nested_tuple)
x = x.replace("(", "")
x = x.replace(")", "")
x = x.replace(", ", ",")
result = eval("(" + x + ")") # Convert the string back to a tuple using eval
print(result)

print("-----")

# 2.Write a Python program to sort a tuple of tuples based on the second element of each tuple.
# Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))

tuple_of_tuples = ((1, 2), (3, 1), (5, 0))
tuple_list = list(tuple_of_tuples)
for i in range(len(tuple_list)):
    for j in range(i + 1, len(tuple_list)):
        if tuple_list[i][1] > tuple_list[j][1]:
            tuple_list[i], tuple_list[j] = tuple_list[j], tuple_list[i]
sorted_tuple_of_tuples = tuple(tuple_list)
print(sorted_tuple_of_tuples)