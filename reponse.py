from abc import ABC, abstractmethod


## Exercice 1:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

## Exercice 2: 
class BankAccount():
    balance = 0

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, amount):
        self.balance += amount
        return self
    
    def __sub__(self, amount):
        self.balance -= amount
        return self
    
## Exercice 3:
def check_positive(func):
    def wrapper(number):
        if number < 0:
            raise ValueError("Number must be positive")
        return func(number)
    return wrapper

## Exercice 4:
class Car:
    _speed = 0

    def __init__(self):
        pass

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value < 1 or value > 200:
            raise ValueError("Speed must be between 1 and 200")
        self._speed = value


## Exercice 5:
class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0 or age > 150:
            raise AgeError("Age must be between 0 and 150")
        self.age = age

class AgeError(Exception):
    pass


## Exercice 6:
class DatabaseConnection:
    entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_by_id(self, id):
        self.entries = [entry for entry in self.entries if entry["id"] != id]

    def drop_all(self):
        self.entries = []

class DbContext:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        pass

## Exercice 7:
class ShapeFactory:
    @staticmethod
    def create(shape, **kwargs):
        if shape == "circle":
            return Circle(kwargs["radius"])
        elif shape == "rectangle":
            return Rectangle(kwargs["width"], kwargs["height"])
        else:
            raise ValueError("Invalid shape")
        
## Exercice 8:
import time
import threading

def timeout_limit(timeout, raise_exception=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if raise_exception:
                def target():
                    nonlocal result
                    result = func(*args, **kwargs)

                thread = threading.Thread(target=target)
                thread.start()

                thread.join(timeout)

                if thread.is_alive():
                    raise TimeoutError("Function took too long")
                
                return result
            else:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                if end - start > timeout:
                    raise TimeoutError("Function took too long")
                return result
        return wrapper
    return decorator

##Exercice 9:
class Matrix:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            raise ValueError("Matrices must have the same size")
        result = [[self.values[i][j] + other.values[i][j] for j in range(len(self.values[0]))] for i in range(len(self.values))]
        return Matrix(result)
    
    def __mul__(self, other):
        if len(self.values[0]) != len(other.values):
            raise ValueError("Matrices must have compatible sizes")
        result = [[sum([self.values[i][k] * other.values[k][j] for k in range(len(self.values[0]))]) for j in range(len(other.values[0]))] for i in range(len(self.values))]
        return Matrix(result)

## Exercice 10:
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
class AnimalFactory:
    @staticmethod
    def create(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError("Invalid animal type")
        

## Exercice 11:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price
    
def top_product(products, n):
    return sorted(products, key=lambda x: x.price, reverse=True)[:n]


## Exercice 12:
class Account():
    def __init__(self, balance):
        self.balance = balance
    
    def __sub__(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Not enough funds")
        
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        
        if self.balance - amount < 0:
            raise ValueError("Not enough funds")
        
        self.balance -= amount

## Exercice 13:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
## Exercice 14:


## Exercice 15:
from statistics import mean, median, variance

class Statistics:
    def __init__(self, values):
        self.values = values
    
    def mean(self):
        return mean(self.values)
    
    def median(self):
        return median(self.values)
    
    def variance(self):
        return variance(self.values)
    
## Exercice 16:
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __add__(self, other):
        if other.__class__ != Vector3D:
            raise TypeError("Must be a Vector3D object")
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)