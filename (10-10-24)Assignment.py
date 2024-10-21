"""
1.Create a class Vehicle with attributes brand and year. The class should have a method get_info() that returns the brand and year of the vehicle. Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.
"""
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"{super().get_info()}, Number of Doors: {self.number_of_doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{super().get_info()}, Has Sidecar: {self.has_sidecar}"

car = Car("Toyota", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", 2019, False)
print(car.get_info())
print(motorcycle.get_info())

print("-----")
"""
2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

def play_sound(animal):
    print(animal.make_sound())

play_sound(Dog())
play_sound(Cat())
play_sound(Cow())

print("-----")
"""
3.Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).
"""
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balance() - amount < 500:
            print("Insufficient funds! Minimum balance of $500 required.")
        else:
            self._BankAccount__balance -= amount

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balance() - amount < -1000:
            print("Insufficient funds! Overdraft limit of $1000 exceeded.")
        else:
            self._BankAccount__balance -= amount

savings = SavingsAccount()
savings.deposit(1000)
savings.withdraw(600)
print(savings.get_balance())

current = CurrentAccount()
current.deposit(500)
current.withdraw(1200)
print(current.get_balance())

print("-----")
"""
4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

    def get_salary(self):
        return self.salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}, Programming Language: {self.programming_language}"

manager = Manager("Alice", 90000, "HR")
developer = Developer("Bob", 80000, "Python")
print(manager.get_details())
print(developer.get_details())
manager.increase_salary(10)
print(manager.get_details())

print("-----")
"""
5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method. Demonstrate polymorphism by passing different types of media to this function.
"""
from abc import ABC, abstractmethod

class Media(ABC):
    @abstractmethod
    def play(self):
        pass

class Audio(Media):
    def play(self):
        return "Playing audio file..."

class Video(Media):
    def play(self):
        return "Playing video file..."

class LiveStream(Media):
    def play(self):
        return "Streaming live..."

def start_media(media):
    print(media.play())

start_media(Audio())
start_media(Video())
start_media(LiveStream())

print("-----")
"""
6.Create an abstract class LibraryItem with abstract methods borrow() and return_item(). Then create two subclasses:

Book, with attributes title, author, and num_copies.
DVD, with attributes title, director, and duration.
Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies (for books) or marks the DVD as borrowed.
"""
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies

    def borrow(self):
        if self.num_copies > 0:
            self.num_copies -= 1
            print(f"You have borrowed '{self.title}'.")
        else:
            print("Sorry, this book is currently unavailable.")

    def return_item(self):
        self.num_copies += 1
        print(f"You have returned '{self.title}'.")

class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed the DVD '{self.title}'.")
        else:
            print("Sorry, this DVD is currently borrowed.")

    def return_item(self):
        self.is_borrowed = False
        print(f"You have returned the DVD '{self.title}'.")

def borrow_item(item):
    item.borrow()

book = Book("1984", "George Orwell", 3)
dvd = DVD("Inception", "Christopher Nolan", 148)

borrow_item(book)
borrow_item(book)
borrow_item(book)
borrow_item(book)

borrow_item(dvd)
borrow_item(dvd)