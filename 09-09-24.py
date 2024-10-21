# Functions: A function is a reusable block of code that performs a specific task. It helps to avoid repetitive code and makes the code modular and easy to manage. A function is executed when it is called.

# Function Declaration - In Python, functions are declared using the def keyword followed by the function name and parentheses (). Here's the basic syntax:
def function_name():
    # code block
    pass

print("-----")

# Example: Basic Function Declaration
def greet():
    print("Hello, welcome to Python functions!")

greet()  # Calling the function

print("-----")

# Types of Arguments: Functions can accept inputs, called arguments, to perform tasks based on those inputs. There are different types of arguments in Python:

# 1. Positional Arguments - Positional arguments are passed in the same order in which they are defined. The position of the argument matters.

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)  # Positional arguments
print(result)  # Output: 8

print("-----")

# 2. Keyword Arguments - Keyword arguments are passed by explicitly mentioning the argument name during the function call. This allows you to change the order of arguments.

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Anurag Kumar")  # Keyword arguments

print("-----")

# 3. Default Arguments - Default arguments allow you to provide default values for function parameters. If the argument is not provided during the call, the default value is used.

def greet_person(name="Anurag Kumar"):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
greet_person()         # Output: Hello, Guest!

print("-----")

# 4. Variable-length Arguments (*args) - Variable-length arguments allow you to pass multiple values without specifying the exact number of arguments. These values are collected into a tuple.

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4)
print(result)  # Output: 10

print("-----")

# 5. Keyword Variable-length Arguments (**kwargs) - Keyword variable-length arguments allow you to pass multiple keyword arguments. These arguments are stored in a dictionary.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

print("-----")

print("End of the Day 12 Session")