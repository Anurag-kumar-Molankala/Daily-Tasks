"""" 
1. lambda() Function
The lambda() function in Python is used to create small, anonymous functions on the fly. These functions are usually used for short operations that don't require the complexity of a fully defined function.

Syntax: lambda arguments: expression
It can have multiple arguments but only one expression. The expression is evaluated and returned.
"""
# Using lambda to create a function that adds 10 to a number
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

print("-----")

"""" 
2. filter() Function
The filter() function is used to filter elements from a list (or any iterable) based on a condition. It returns an iterator containing only elements that satisfy the condition.

Syntax: filter(function, iterable)
The function should return True or False for each element in the iterable. Only the elements for which the function returns True are included in the result.
"""
# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

print("-----")

""""
3. map() Function
The map() function is used to apply a function to each item in an iterable (like a list). It returns an iterator with the results of applying the function to each item.

Syntax: map(function, iterable)
The function is applied to each element in the iterable, and the result is returned as a new list (or any other iterator).
"""
# Multiplying each number by 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

print("-----")

print("End of the Day 14 Session")