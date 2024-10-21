"""
1. Constructor in Python:
The constructor creates memory for a new object.
It executes the __init__ method to initialize object variables.
Initialization is the process of assigning values to variables during object creation.
"""

# Class definition
class Person:
    # Constructor method
    def __init__(self, name, age):
        # 'self' is used to assign values to instance variables
        self.name = name  # Initialization: Assign value to 'name'
        self.age = age    # Initialization: Assign value to 'age'

    # Method to display the information of the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the class 'Person'
person1 = Person("Alice", 25)

# Accessing method to display the information of the object
person1.display_info()  # Output: Name: Alice, Age: 25

print("-----")

"""
2. self Keyword:
self is a reference to the current object (instance of the class).
It's mandatory as the first parameter in methods, including the constructor.
self allows accessing instance variables within class methods.
"""

class Car:
    def __init__(self, brand, model):
        # Initializing instance variables
        self.brand = brand
        self.model = model

    def show_car(self):
        # Using self to access instance variables
        print(f"Car: {self.brand} {self.model}")

# Create an object of Car class
car1 = Car("Toyota", "Camry")
car1.show_car()  # Output: Car: Toyota Camry

print("-----")

"""
3. Using a Different Word Instead of self:
In Python, you can use any word instead of self, but it's a convention to use self.
"""
# Example using this instead of self:
class Laptop:
    # Constructor using 'this' instead of 'self'
    def __init__(this, brand, price):
        this.brand = brand
        this.price = price

    def show_laptop(this):
        # Accessing instance variables with 'this'
        print(f"Laptop: {this.brand}, Price: ${this.price}")

# Create an object of Laptop class
laptop1 = Laptop("Dell", 1200)
laptop1.show_laptop()  # Output: Laptop: Dell, Price: $1200

print("-----")

print("End of the Day 18 Session")