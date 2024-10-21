"""
Object-Oriented Programming (OOP) is a programming paradigm where everything is represented as objects. 
It is based on real-world entities like objects, which have attributes (properties) and behaviors (methods). 
The two fundamental concepts in OOP are Classes and Objects.

1. Class:
A Class is like a blueprint or template for creating objects. 
It defines the structure (attributes) and behaviors (methods) that the objects created from the class will have.

Think of a class as a blueprint for a house. 
It defines how the house will look (structure) and what it can do (behavior), but it's not a house itself—it's just a plan.

2. Object:
An Object is an instance of a class. 
When you create an object from a class, it's like building a house from the blueprint. 
The object now exists with the structure and behaviors defined in the class.

Each object can have different values for its attributes, but they all share the same structure and behavior defined by the class.
"""
# Define a class called Car (blueprint)
class Car:
    # Constructor method to initialize object properties
    def __init__(self, brand, model, year):
        self.brand = brand   # Attribute (property)
        self.model = model   # Attribute (property)
        self.year = year     # Attribute (property)

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)  # Object 1
car2 = Car("Honda", "Civic", 2019)     # Object 2

# Call the method on both objects to display car details
car1.display_info()  # Output: Car: Toyota Corolla, Year: 2020
car2.display_info()  # Output: Car: Honda Civic, Year: 2019

print("-----")

print("End of Day 17 Session")