"Notes on Lists in Python"
# How to Make a List - A list in Python is a collection of elements that can be of different data types (e.g., integers, strings, etc.). Lists are mutable, meaning you can modify them after creation.
# Creating a list using split()
user_input = input("Enter numbers separated by spaces: ")  # e.g., 1 2 3 4 5
num_list = user_input.split()  # ['1', '2', '3', '4', '5']
print(num_list)

print("-----")

# Accessing Elements from the List - Elements in a list can be accessed using their index, where indexing starts at 0.
num_list = ['1', '2', '3', '4', '5']
print("First element:", num_list[0])  # Output: '1'
print("Last element:", num_list[-1])  # Output: '5'

print("-----")

# Adding New Elements to the List - You can add elements to a list using different methods.
#1. Append(): Adds a new element at the end of the list.
num_list = ['1', '2', '3']
num_list.append('4')
print(num_list)  # Output: ['1', '2', '3', '4']

print("-----")

#2. Insert(): Adds a new element at a specified index position.
num_list.insert(1, '1.5')
print(num_list)  # Output: ['1', '1.5', '2', '3', '4']

print("-----")

#3. Extend(): Adds elements from one list to another.
another_list = ['5', '6']
num_list.extend(another_list)
print(num_list)  # Output: ['1', '1.5', '2', '3', '4', '5', '6']

print("-----")

# Iterating Through the List - You can loop through elements in a list using a for loop.
for item in num_list:
    print(item)

print("-----")

# Removing Elements from the List - You can remove elements from a list using various methods.
#1. Pop() - Removes and returns the last element from the list.
last_item = num_list.pop()
print("Removed:", last_item)  # Output: '6'
print(num_list)  # Output: ['1', '1.5', '2', '3', '4', '5']

print("-----")

#2. Remove() - Removes the first occurrence of a specified element.
num_list.remove('1.5')
print(num_list)  # Output: ['1', '2', '3', '4', '5']

print("-----")

#3. Clear() - Removes all elements from the list.
num_list.clear()
print(num_list)  # Output: []

print("-----")

#4. Del - Deletes the entire list.
del num_list

print("-----")

# Aliasing and Cloning of the List:
#1. Aliasing - Creating another name for the same list.
original_list = ['a', 'b', 'c']
alias_list = original_list
alias_list.append('d')
print(original_list)  # Output: ['a', 'b', 'c', 'd']

print("-----")

#2. Cloning - Creating a copy of the list using slicing.
original_list = ['a', 'b', 'c']
clone_list = original_list[:]
clone_list.append('e')
print(original_list)  # Output: ['a', 'b', 'c']
print(clone_list)     # Output: ['a', 'b', 'c', 'e']

print("-----")

# Ordering of the List:
#1. Reverse() - Reverse the order of the list elements.
num_list = ['1', '2', '3', '4', '5']
num_list.reverse()
print(num_list)  # Output: ['5', '4', '3', '2', '1']

print("-----")

#2. Sort() - Sorts the list in ascending order.
num_list = [3, 1, 4, 2, 5]
num_list.sort()
print(num_list)  # Output: [1, 2, 3, 4, 5]

print("-----")

print("End of the Day 7 Session")