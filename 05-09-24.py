# Dictonay - A dictionary is a data structure in Python that stores a collection of key-value pairs. It is an unordered collection of key-value pairs where each key is unique and maps to a specific value. Dictionaries are also known as associative arrays, hash tables, or maps.

# Create an empty dictionary
my_dict = {}
print(my_dict)

print("-----")

# Create a dictionary with key-value pairs
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)

print("-----")

# Create a dictionary using the dict keyword
my_dict = dict(name='John', age=30, city='New York')
print(my_dict)

print("-----")

# Access elements using their keys
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 30
print(my_dict['city'])  # Output: New York

print("-----")

# Update elements using their keys
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict['name'] = 'Jane'
my_dict['age'] = 31
my_dict['city'] = 'Los Angeles'

print(my_dict)  # Output: {'name': 'Jane', 'age': 31, 'city': 'Los Angeles'}

print("-----")

# Deleting Elements
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Delete elements using the pop() method
my_dict.pop('city')

print(my_dict)  # Output: {'name': 'John'}

print("-----")

# Delete elements using the del statement
del my_dict['age']

print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

print("-----")

# Dictonary Funtions - Dictionaries have several built-in functions that can be used to manipulate and access elements. Here are some of the most commonly used functions:

# Create a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Keys() - Returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

print("-----")

# Values() - Returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])

print("-----")

# key-value pairs - Returns a view object that displays a list of all the key-value pairs in the dictionary.
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

print("-----")

# Clear() - Removes all items from the dictionary.
my_dict.clear()

print(my_dict)  # Output: {}

print("-----")

# Copy() - Returns a shallow copy of the dictionary.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict_copy = my_dict.copy()

print(my_dict_copy)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

print("-----")

# Update() - Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.update({'country': 'USA'})

print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

print("-----")

# Popitem() - The popitem() method removes and returns the last inserted key-value pair. If the dictionary is empty, it raises a KeyError.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

print(my_dict.popitem())  # Output: ('city', 'New York')

print(my_dict)  # Output: {'name': 'John'}

print("-----")

print("End of the Day 11 Session")