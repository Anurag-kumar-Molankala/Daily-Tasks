# Types of Variables

"""
1. Instance Variables
Declaration:

Inside the constructor using self.
Inside an instance method using self.
By directly using the self keyword.

Accessing:

Inside the class using self.
Outside the class using an object reference variable (orv) or class name.
"""
class Person:
    # Declaring an instance variable inside the constructor
    def __init__(self, name, age):
        self.name = name  # Instance variable declared using self
        self.age = age    # Instance variable declared using self

    # Instance method
    def update_age(self, new_age):
        # Declaring an instance variable inside an instance method
        self.age = new_age

# Creating an object of the Person class
person1 = Person("Alice", 25)

# Accessing instance variables inside the class
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25

# Modifying instance variable through method
person1.update_age(30)
print(person1.age)   # Output: 30

# Accessing instance variable outside of the class using ORV
print(person1.name)  # Output: Alice

print("-----")

"""
2. Static Variables
Declaration:

Directly inside the class.
Inside the constructor using the class name.
Inside an instance method using the class name.

Accessing:

Inside the constructor using the class name.
Inside an instance method using self.
Outside the class using an object reference variable (orv) or class name.
"""
class Student:
    # Static variable declared inside the class
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name
        # Declaring static variable inside constructor using class name
        Student.school_code = "S123"

    def display_info(self):
        # Accessing static variable inside instance method using class name
        print(f"Student: {self.name}, School: {Student.school_name}")

# Creating an object of the Student class
student1 = Student("Bob")

# Accessing static variables inside the class
student1.display_info()  # Output: Student: Bob, School: ABC School

# Accessing static variable outside the class using ORV
print(student1.school_name)  # Output: ABC School

# Accessing static variable outside the class using class name
print(Student.school_code)   # Output: S123

print("-----")

"""
3. Local Variables
Declaration:
Declared inside a method directly.

Accessing:
Local variables can only be accessed inside the method they are declared in.
To make a local variable accessible globally, convert it to a global variable using the global keyword.
"""
class Calculator:
    def add(self, a, b):
        # Local variable inside the method
        result = a + b
        print(f"Result: {result}")

# Creating an object of the Calculator class
calc = Calculator()
calc.add(5, 3)  # Output: Result: 8

# Trying to access the local variable outside the method will give an error
# print(result)  # This will raise an error since `result` is local to the method

print("-----")

# Converting Local Variable to Global
class GlobalExample:
    def make_global(self):
        # Declare a local variable
        local_var = "I'm local!"
        
        # Convert it to a global variable
        global global_var
        global_var = "I'm global now!"

# Creating an object
obj = GlobalExample()
obj.make_global()

# Accessing the global variable outside the method
print(global_var)  # Output: I'm global now

print("-----")

print("End of the Day 19 Session")
