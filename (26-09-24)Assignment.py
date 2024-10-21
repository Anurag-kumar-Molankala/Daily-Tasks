"""1.Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information."""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def update_age(self, new_age):
        self.age = new_age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

person1 = Person("Alice", 25, "Female")
person2 = Person("Bob", 30, "Male")
person3 = Person("Charlie", 22, "Male")

person1.update_age(26)
person1.display_info()  
person2.display_info()
person3.display_info()

print("-----")

"""2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others."""

class Company:
    total_employees = 0
    
    def __init__(self, name, department):
        self.name = name
        self.department = department
        Company.total_employees += 1 
    def display_info(self):
        print(f"Employee: {self.name}, Department: {self.department}")

employee1 = Company("Alice", "HR")
print("Total employees:", Company.total_employees)
employee2 = Company("Bob", "Finance")
print("Total employees:", Company.total_employees)
employee3 = Company("Charlie", "IT")
print("Total employees:", Company.total_employees)

employee1.total_employees = 100
print("Total employees:", Company.total_employees)

print("-----")

"""3.Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle."""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"Area of rectangle: {area}")

rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)
rect3 = Rectangle(6, 2)

rect1.calculate_area()
rect2.calculate_area()
rect3.calculate_area()

print("-----")

"""4.Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe"""

class Employee:
    bonus = 5000
    
    def __init__(self, salary):
        self.salary = salary
    
    def total_salary(self):
        total = self.salary + Employee.bonus
        print(f"Total salary (with bonus): {total}")

emp1 = Employee(30000)
emp2 = Employee(40000)
emp3 = Employee(50000)

emp1.total_salary()
emp2.total_salary()
emp3.total_salary()

Employee.bonus = 8000
emp1.total_salary()
emp2.total_salary()
emp3.total_salary()