"""
Create a dictionary where the keys are tuples representing coordinates (x, y) and the values are city names. 
Write a Python program to print the city name for a given coordinate. 
Example Dictionary: #{(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"} 
# Input: (40.7128, -74.0060) # Expected Output: "New York"
"""
my_dict = {(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}
print(my_dict[40.7128, -74.0060])

print("-----")

"""
Write a Python program to sort a tuple of tuples based on the second element of each tuple.
# Example Tuple: ((1, 2), (3, 1), (5, 0)) 
# Expected Output: ((5, 0), (3, 1), (1, 2))
"""

tuple_of_tuples = ((1, 2), (3, 1), (5, 0))
tuple_list = list(tuple_of_tuples)
for i in range(len(tuple_list)):
    for j in range(i + 1, len(tuple_list)):
        if tuple_list[i][1] > tuple_list[j][1]:
            tuple_list[i], tuple_list[j] = tuple_list[j], tuple_list[i]
sorted_tuple_of_tuples = tuple(tuple_list)
print(sorted_tuple_of_tuples)

print("-----")

"""
Write a Python program to find the minimum and maximum elements in a tuple of integers. 
# Example Tuple: (10, 20, 5, 40, 25) 
# Expected Output: Min: 5, Max: 40
"""
my_tuple = (10, 20, 5, 40, 25)
i = min(my_tuple) 
j = max(my_tuple)
print("Min:", i , "Max:", j)

print("-----")

"""
Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple. 
# Example Tuple: (1, (2, 3), (4, 5, 6)) 
# Expected Output: (1, 2, 3, 4, 5, 6)
"""
nested_tuple = (1, (2, 3), (4, 5), 6)
x = str(nested_tuple)
x = x.replace("(", "").replace(")", "").replace(", ", ",")
result = eval(x)
print(result)