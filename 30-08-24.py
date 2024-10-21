#1. Mathematical Operations on Lists - You can perform mathematical operations (like addition, subtraction, multiplication) on the elements of a list. Note that these operations are usually element-wise and the list should contain numbers.

# Add a constant value to each element in the list.

# Taking user input to create a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("-----")

# Adding 5 to each element in the list
updated_numbers = [num + 5 for num in numbers]

print("Original List:", numbers)
print("Updated List:", updated_numbers)

print("-----")

#2. Membership Checking - Membership checking involves verifying if an element exists in a list. This is done using the in or not in operators.

# Check if a number is in the list.
# Taking user input to create a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("-----")

# Taking user input for the number to check
check_num = int(input("Enter the number to check: "))

print("-----")

# Checking membership
if check_num in numbers:
    print(f"{check_num} is in the list.")
else:
    print(f"{check_num} is not in the list.")

print("-----")

#3. Nested Lists - A nested list is a list that contains other lists as its elements. This allows for multi-dimensional data structures like matrices.

# Create a 2x2 matrix using nested lists.
# Taking user input to create a 2x2 matrix
matrix = []
for i in range(2):
    row = list(map(int, input(f"Enter 2 numbers for row {i+1}, separated by space: ").split()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)

print("-----")

#4. List Comprehension - List comprehension is a concise way to create lists. It allows you to generate a new list by applying an expression to each element of an existing list or any iterable.

# Create a list of squares of numbers.
# Taking user input to create a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("-----")

# Using list comprehension to create a list of squares
squares = [num**2 for num in numbers]

print("List of Squares:", squares)

print("-----")

print("End of the Day 8 Session")