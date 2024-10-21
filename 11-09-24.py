# Types of Variables

# 1. Global Variables - A global variable is declared outside of any function or block of code. It is accessible throughout the entire program, including within functions.

x = 10  # Global variable

def display():
    print("Global x:", x)  # Can access the global variable inside the function

display()
print("Global x outside function:", x)

print("-----")

# 2. Local Variables - A local variable is declared inside a function and is only accessible within that function. Once the function execution is complete, the variable is deleted and cannot be accessed outside the function.

def display():
    y = 20  # Local variable
    print("Local y:", y)

display()
# print(y)  # This will give an error because 'y' is local to the display function.

print("-----")

# 3. Nested Variables - Nested variables refer to variables in nested (inner) functions. In such cases, a variable declared in the outer function can be accessed in the inner function, but a variable in the inner function cannot be accessed in the outer function.

def outer():
    a = 30  # Variable in the outer function

    def inner():
        print("Accessing 'a' from outer function:", a)  # Accessing outer variable

    inner()  # Calling the inner function

outer()

print("-----")

print("End of the Day 13 Session")