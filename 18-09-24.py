""""
Python Modules Overview
A module is a collection of functions, classes, variables, or even other Python files that are grouped together to organize code into manageable and reusable components. Modules help break down large programs and make code more readable and maintainable.
"""
# Types of Modules:

#  Built-in Modules: These are pre-installed with Python and provide essential functionality.

# 1. OS Module - The OS module in Python allows interaction with the operating system, like handling files or directories.

import os

# Get the current working directory
print(os.getcwd())

# List files and directories in the current directory
print(os.listdir())

print("-----")

# 2. Math Module - The Math module provides mathematical functions, such as trigonometry, logarithms, and basic calculations.

import math

# Find the square root of 16
print(math.sqrt(16))

# Get the value of pi
print(math.pi)

print("-----")

# 3. Datetime Module - The Datetime module deals with date and time operations.

import datetime

# Get the current date and time
current_time = datetime.datetime.now()
print(current_time)

# Get the current date only
current_date = datetime.date.today()
print(current_date)

print("-----")

# 4. Random Module - The Random module is used to generate random numbers or choose random elements from a sequence.

import random

# Generate a random number between 1 and 10
print(random.randint(1, 10))

# Choose a random element from a list
colors = ['red', 'blue', 'green']
print(random.choice(colors))

print("-----")

# Custom Modules: You can create your own modules based on your requirements. For example, let's create a module named my_module.py:

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

print("-----")

# You can now import this module into another Python file:

import my_module

# Call the functions from the custom module
print(my_module.greet("Alice"))
print(my_module.add(2, 3))

print("-----")

# Third-party Modules: These are not included with Python by default but can be installed via pip. Examples include Requests (for HTTP requests) and Pandas (for data manipulation).

# 1. Requests Module - Used for making HTTP requests, such as fetching data from websites.

import requests

# Fetch data from a website
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.json())

print("-----")

# 2. Pandas Module - Used for data manipulation and analysis.

import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

print("-----")

print("End of the Day 15 Session")