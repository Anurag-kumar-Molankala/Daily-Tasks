# 1. Add a key to a dictionary

my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

print("-----")

# 2. Check if a value is present in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
value = 2
if value in my_dict.values():
    print(True)  # Output: True
else:
    print(False)

print("-----")

# 3. Create a dictionary with keys as numbers between 1 and 15 and values as their squares.

my_dict = {}
for i in range(1, 16):
    my_dict[i] = i**2
print(my_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

print("-----")

# 4. Create a dictionary from a string, tracking the count of each letter

s = 'w3resource'
my_dict = {}
for char in s:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1
print(my_dict)  # Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

print("-----")

# 5. Combine two dictionaries by adding values of common keys

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
for key, value in dict2.items():
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value
print(dict1)  # Output: {'a': 1, 'b': 5, 'c': 4}

print("-----")

# 6. Merge two Python dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("-----")

# 7. Sort a dictionary by keys or values

my_dict = {'c': 3, 'b': 2, 'a': 1}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

print("-----")

# 8. Write a Python program to create a dictionary from a string.

s = 'w3resource'
my_dict = {}
for char in s:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1
print(my_dict)  # Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}