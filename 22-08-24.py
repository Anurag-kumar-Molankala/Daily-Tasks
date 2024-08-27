#By this code we will get list of Keywords that are used in Python.
help('keywords')

print("-----")

"""
1. False - Represents the boolean value `False`.

2. None - Represents the absence of a value or a null value.

3. True - Represents the boolean value `True`.

4. and - Logical operator that returns `True` if both operands are `True`.

5. as - Used to create an alias when importing a module.

6. assert - Used for debugging purposes to test if a condition is `True`.

7. async - Used to define an asynchronous function (used with `await`).

8. await - Used to pause the execution of an `async` function until the result is available.

9. break - Terminates the current loop.

10. class - Used to define a new user-defined class.

11. continue - Skips the rest of the code inside a loop for the current iteration only.

12. def - Used to define a new function.

13. del - Used to delete an object or variable.

14. elif - Used for conditional branching (else if).

15. else - Used in conditional branching, to define the block of code to be executed if the condition is `False`.

16. except - Used to catch and handle exceptions (errors) in a `try` block.

17. finally - Defines a block of code that will be executed no matter what after a `try` block.

18. for - Used to create a `for` loop to iterate over a sequence (like a list, tuple, etc.).

19. from - Used in import statements to import specific parts from a module.

20. global - Declares that a variable inside a function is global (i.e., it should not be local).

21. if - Used to make a decision in code, executing a block if the condition is `True`.

22. import - Used to include the module in the current script.

23. in - Used to check if a value exists within a sequence (like a list, string, etc.).

24. is - Tests for object identity, checking if two variables refer to the same object.

25. lambda - Used to create small, anonymous functions (i.e., functions without a name).

26. nonlocal - Declares a variable inside a nested function that refers to a variable in the enclosing function.

27. not - Logical operator that returns `True` if the operand is `False`.

28. or - Logical operator that returns `True` if at least one of the operands is `True`.

29. pass - A null statement; used as a placeholder in functions, loops, etc., where code is syntactically required but you want nothing to happen.

30. raise - Used to raise an exception.

31. return - Exits a function and optionally passes back an expression to the caller.

32. try - Used to catch exceptions (errors) by running code that might raise an error.

33. while - Used to create a `while` loop, which executes as long as a condition is `True`.

34. with - Used to wrap the execution of a block of code with methods defined by a context manager (e.g., file operations).

35. yield - Used to pause and resume a generator function.
"""
#Operators

#Arithmetic Operator: Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.

#1. Addition:
add1 = int(input("Enter num1 value:"))
add2 = int(input("Enter num2 value:"))
add_result = add1 + add2
print("The Sum is:", add_result)

#2. Multipliation:
multi1 = float(input("Enter num1 value:"))
multi2 = float(input("Enter num2 value:"))
multi_result = multi1 * multi2
print("The Multiple is:", multi_result)

#3. Subtraction:
sub1 = complex(input("Enter num1 value:"))
sub2 = complex(input("Enter num2 value:"))
sub_result = sub1 - sub2
print("The Subtraction is:", sub_result)

#4. Division:
div1 = int(input("Enter num1 value:"))
div2 = int(input("Enter num2 value:"))
div_result = div1 - div2
print("The Division is:", div_result)

print("-----")

#Logical Operator: Logical operators are used to perform logical operations and return boolean values (True or False).

#1. AND:
num1 = int(input("Entr the num1:"))
num2 = int(input("Enter the num2:"))
if num1 > 0 and num2 > 0:
    print("Both numbers are true.")
elif num1 < 0 and num2 < 0:
    print("Both numbers are false.")
else:
    print("One number is True and the other number is False.")

#2. OR:
num1 = int(input("Entr the num1:"))
num2 = int(input("Enter the num2:"))
if num1 > 0 or num2 > 10:
    print("Both numbers are true.")
elif num1 < 0 or num2 < 10:
    print("Both numbers are false.")
else:
    print("One number is True and the other number is False.")

print("-----")

# Relational Operator: Relational operators are used to compare two values and return a boolean result (True or False).

# >; >=; <; <=; ==; !=

# Example 1: >
x = int(input("Enter a number: "))
if x > 10:
    print("The number is greater than 10.")
else:
    print("The number is not greater than 10.")

# Example 2: >=
y = int(input("Enter a number: "))
if y >= 5:
    print("The number is greater than or equal to 5.")
else:
    print("The number is less than 5.")

# Example 3: <
a = int(input("Enter a number: "))
if a < 0:
    print("The number is less than 0.")
else:
    print("The number is not less than 0.")

# Example 4: <=
b = int(input("Enter a number: "))
if b <= 100:
    print("The number is less than or equal to 100.")
else:
    print("The number is greater than 100.")

# Example 5: ==
c = int(input("Enter a number: "))
if c == 50:
    print("The number is equal to 50.")
else:
    print("The number is not equal to 50.")

# Example 6: !=
d = int(input("Enter a number: "))
if d != 7:
    print("The number is not equal to 7.")
else:
    print("The number is equal to 7.")

print("-----")

#Identity Operator: Identity operators are used to compare the memory locations of two objects. The two identity operators are is and is not.
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)     # Output: False (a and b are different objects in memory)
print(a is c)     # Output: True  (a and c refer to the same object)
print(a is not b) # Output: True  (a and b are different objects)

print("-----")

#Bitwise Operator: Bitwise operators are used to perform operations on binary representations of integers.
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(a & b)  # Output: 0   (Binary: 0000)
print(a | b)  # Output: 14  (Binary: 1110)
print(a ^ b)  # Output: 14  (Binary: 1110)
print(~a)     # Output: -11 (Binary: ...11110101, two's complement representation)
print(a << 1) # Output: 20  (Binary: 10100)
print(a >> 1) # Output: 5   (Binary: 0101)

print("-----")

#Membership Operator: Membership operators are used to test if a value or variable is found in a sequence (such as a list, tuple, or string). The operators are "in" and "not in".
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)     # Output: True
print(6 in numbers)     # Output: False
print(3 not in numbers) # Output: False
print(6 not in numbers) # Output: True

print("-----")

#Assignment Operator: Assignment operators are used to assign values to variables.
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

x -= 2  # Equivalent to x = x - 2
print(x)  # Output: 6

x *= 4  # Equivalent to x = x * 4
print(x)  # Output: 24

x /= 2  # Equivalent to x = x / 2
print(x)  # Output: 12.0

x %= 5  # Equivalent to x = x % 5
print(x)  # Output: 2.0

x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 8.0

x //= 4  # Equivalent to x = x // 4
print(x)  # Output: 2.0

print("-----")

#ASCII: ASCII (American Standard Code for Information Interchange) is a character encoding standard that represents text in computers and other devices.
"""
Uppercase Letters (A-Z, 65-90)
Lowercase Letters (a-z, 97-122)
"""
#For example, in Python, you can use the ord() function to get the ASCII value of a character:
print(ord('A'))  # Outputs: 65
print(ord('Z'))  # Outputs: 90

print("-----")

print(ord('a'))  # Outputs: 97
print(ord('z'))  # Outputs: 122

#And you can use chr() to convert an ASCII value back to a character:
print(chr(65))  # Outputs: 'A'
print(chr(90))  # Outputs: 'Z'

print("-----")

print(chr(97))  # Outputs: 'a'
print(chr(122)) # Outputs: 'z'

#ASCII is fundamental to computing and helps ensure consistent text representation across different systems.

print("-----")

print("End of the Day 2 Session")