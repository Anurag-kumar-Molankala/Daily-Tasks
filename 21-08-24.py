print ("Hello World!") # Here I have just printed Hello World!

print("-----")

# For Single Line comment we use "#"

"""" For Mutliline Comments we use three double quotes.
     We can write multiple line in between this quotes.
 """

'''' Even we use three single quotes for multiple line comments/string.'''

# Variables - It's a container to store the values.

#Example
name = "Anurag Kumar"
print (name)

print("------")

x = 10
y = 20
print (x + y)

print("------")

# Identifiers - Words define by the programmer that meaning can be changed from time - to - time.

# 1. Variables:

x = 10  # 'x' is an identifier for a variable that stores the value 10
name = "John"  # 'name' is an identifier for a variable that stores the string "John"

# 2. Functions:

def greet():
    print("Hello, World!")  # 'greet' is an identifier for this function
greet()  # Calling the function 'greet'

print("------")

# 3. Classes:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model  # 'Car' is an identifier for this class

my_car = Car("Toyota", "Corolla")  # Creating an instance of the 'Car' class

"""" 
Rules to declare a Identifiers:

1. Identifiers can be a combination of letters (a-z, A-Z), digits (0-9), and underscores (_).

2. Identifiers cannot start with a digit.
        For example, 123abc is not a valid identifier, but abc123 is.

3.Identifiers are case-sensitive.
    For example, MyVar and myvar are considered two different identifiers.

4. Keywords cannot be used as identifiers.
    For example, if, while, class, def, etc., cannot be used as identifiers.

- Valid Identifiers:

1. my_var
2. CarModel
3. _temp
4. data2

- Invalid Identifiers:

1. 2data - starts with a digit
2. my-var - contains a hyphen
3. class - a reserved keyword in Python

"""

# How to know the ID:

domain = "Nama Bengaluru"
print(id(domain))

print ("------")

animal = "Dog"
print(id(animal))

print ("------")

# Types of Variables:

# 1. String ("str"): A string is a sequence of characters enclosed within single (') or double (") quotes.
name = "Bala Ram" 

# 2. Integer (int): An integer is a whole number, positive or negative, without decimals.
age = 24

# 3. Float (float): A float is a number, positive or negative, containing one or more decimals.
price = 19.99

# 4. Boolean (bool):  A boolean variable can hold one of two values: True or False.
the_student = True

# 5. List: A list is an ordered collection of items, which can be of different types. Lists are created using square brackets [].
fruits = ["apple", "banana", "cherry"]

# 6. Tuple: A tuple is similar to a list, but it is immutable, meaning that its values cannot be changed. Tuples are created using parentheses ().
animals = ("Lion, Tiger, Cheetha")

# 7. Set: A set is an unordered collection of unique items. Sets are created using curly braces {}.
colors = {"red", "green", "blue"}

# 8. Dictionary (dict): A dictionary is a collection of key-value pairs. Each key is associated with a value. Dictionaries are created using curly braces {}.
student = {"name": "Anurag", "age": 22, "is_graduated": True}

print (name)
print(age)
print(price)
print(the_student)
print(fruits)
print(animals)
print(colors)
print(student)

print("--------")

# How to know the "Type/Data type" of the data we are typing.
place = ("Hyderabad")
print(type(place))

phn_no = (9618325160)
print(type(phn_no))

print("------")

print("End on the Day 01 - Session.")