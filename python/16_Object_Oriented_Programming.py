# Object Oriented Programming

print("Class ")

class lol:
    def demo():
        print("chirag")
c=lol
c.demo()

# class with "__--init--__ and __self__

class emp:
    company = "hp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def print(self):
        print(f"{self.name} work in {self.company} company with {self.salary} salary")
e = emp("chirag" , 100000)
e.print()

print("@Staticmethod")

class empl:
    def __init__(self,name):
        self.name=name
    def print(self):
        print(f"my name is {self.name}")
    @staticmethod
    def lol():
        print("LOL")
g=empl("chirag")
g.print()
g.lol()

print("@Classmethos")

class emplo:
    name = "chirag"
    def __init__(self,lname):
        self.lname=lname
    def print(self):
        print(f"my lastname is {self.lname}")
    @classmethod
    def lol(cls):
        print(f"my name is {cls.name}")
g=emplo("suthar")
g.lol()
g.print()

print("Inheritance (Reusing Code)")

class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):  # Inheriting from Animal
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())  # Output: Bark

print("Multiple Inheritance")

class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):  # Multiple Inheritance
    pass

obj = C()
print(obj.method_a())  # Output: Method A
print(obj.method_b())  # Output: Method B

print("Polymorphism (Same Method, Different Behavior)")

class Bird:
    def fly(self):
        return "Birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

bird = Bird()
penguin = Penguin()

print(bird.fly())      # Output: Birds can fly
print(penguin.fly())   # Output: Penguins cannot fly

print("Abstraction (Hiding Implementation Details)")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # No implementation

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  # Implemented in child class

square = Square(5)
print(square.area())  # Output: 25

print("Magic Methods (Dunder Methods) ")

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):  # String representation
        return f"Book: {self.title}"

    def __len__(self):  # Define behavior for len()
        return self.pages

book = Book("Python Basics", 300)
print(str(book))  # Output: Book: Python Basics
print(len(book))  # Output: 300

print("Class vs. Static Methods")

class Example:
    class_var = "I am a class variable"

    def instance_method(self):
        return "Instance Method"

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    def static_method():
        return "Static Method"

obj = Example()
print(obj.instance_method())  # Output: Instance Method
print(Example.class_method()) # Output: I am a class variable
print(Example.static_method()) # Output: Static Method