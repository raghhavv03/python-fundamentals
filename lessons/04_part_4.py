from abc import ABC, abstractmethod


# OOP
# Classes are blueprints for creating objects. They define the properties and behaviors of the objects
# An object is an instance of a class. It is created using the class and has its own unique identity and state
class Student:
    subject = "python"
    college = "abc university"


student1 = Student()  # Creating an object of the Student class
student2 = Student()
print(student1)  # The object is stored in memory and has a unique id
print(student2)
print(
    student1.subject, student1.college
)  # We can access the properties of the object using dot notation

list1 = [1, 2, 3, 4, 5]
print(
    type(list)
)  # The type of the object is list. Python has built-in classes for different data types like int, float, str, list, dict, set, etc. We can also create our own classes
set1 = set()  # We can create an empty set using set method of class set


# Constructors
class Student:
    college = "abc university"

    def __init__(self, name, age):  # 'self' refers to the instance.
        self.name = name  # Assign instance properties.
        self.age = age
        print("Constructor called")  # Constructor runs on instance creation.


student1 = Student(
    "alice", 20
)  # Creating an object of the Student class and passing arguments to the constructor
student2 = Student("bob", 22)
# Use default parameter values rather than multiple constructors.

# Attributes
# Class attributes are shared by all objects of the class, they are defined outside the constructor and are accessed using the class name or the object name
# Instance attributes are unique to each object, they are defined in the constructor and are accessed using the object name
print(Student.college)  # We can access the class attribute using the class name
print(student1.name)  # We can access the instance attribute using the object name
# print(Student.name) # We cannot access the instance attribute using the class name, it will raise an AttributeError


# Methods
class Laptop:
    storage_type = "SSD"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod  # Decorator to define a class method
    def get_storage_type(
        cls,
    ):  # Class method, it is a method that is defined in the class and is called using the class name
        print(f"The storage type of the laptop is {cls.storage_type}.")

    def laptop_info(
        self,
    ):  # Instance method, it is a method that is defined in the class and is called using the object
        print(
            f"The laptop has {self.ram} gb of ram and {self.storage} gb of {self.storage_type}."
        )

    @staticmethod  # Decorator to define a static method
    def discount(
        price, percentage
    ):  # Static method, it is a method that is defined in the class and is called using the class name. It does not have access to the class attributes or instance attributes
        discounted_price = price - (price * percentage / 100)
        print(f"The discounted price is {discounted_price}.")


laptop1 = Laptop(16, 512)
laptop2 = Laptop(8, 256)
laptop1.laptop_info()
Laptop.get_storage_type()  # We can call the class method using the class name
laptop1.get_storage_type()  # We can also call the class method using the object name
Laptop.discount(1000, 10)  # We can also call the static method using the class name
laptop1.discount(1000, 10)  # We can call the static method using the object name


# Create an online store for products
class Product:
    count = 0  # Class attribute to keep track of the number of products created

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1  # Increment the count of products created

    def product_info(self):
        print(f"The product name is {self.name} and the price is {self.price}.")

    @classmethod
    def product_count(cls):
        print(f"The number of products created is {Product.count}.")

    @staticmethod
    def calculate_discount(price, percentage):
        discounted_price = price - (price * percentage / 100)
        print(f"The discounted price is {discounted_price}.")


p1 = Product("laptop", 1000)
p2 = Product("phone", 500)
p3 = Product("tablet", 300)
p1.product_info()
Product.product_count()
p1.product_count()
Product.calculate_discount(1000, 10)
p1.calculate_discount(
    p1.price, 10
)  # We can also dynamically pass the price of the product to the static method


# OOP pillars
# Encapsulation: it is the process of hiding the internal details of an object and only exposing the necessary information to the outside world
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Private attribute

    def set_balance(self, balance):  # Setter method to modify the private attribute
        if balance < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = balance

    def get_balance(self):  # Getter method to access the private attribute
        return self.__balance


account1 = BankAccount("alice", 1000)
print(
    account1.get_balance()
)  # We can access the private attribute using the getter method
account1.set_balance(
    1500
)  # We can modify the private attribute using the setter method
print(
    account1.name, account1.BankAccount__balance
)  # We cannot access the private attribute directly, it will raise an AttributeError, but we can access it using name mangling, it is not recommended to do so


# Inheritance: it is the process of creating a new class that is a modified version of an existing class
class Employee:
    start_time = "9 am"
    end_time = "5 pm"

    def change_shift(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class Teacher(
    Employee
):  # Teacher class inherits the properties of the Employee class, it is called a child class or subclass, Employee is the parent class or superclass
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


t1 = Teacher("alice", "math")
print(
    t1.name, t1.subject, t1.start_time, t1.end_time
)  # The Teacher class inherits the properties of the Employee class, we can access the class attributes of the Employee class using the object of the Teacher class
t1.change_shift(
    "8 am", "4 pm"
)  # We can also call the method of the Employee class using the object of the Teacher class


# Types of inheritance
class Employee:
    start_time = "9 am"
    end_time = "5 pm"


class AdminStaff(
    Employee
):  # Single inheritance, AdminStaff class inherits from Employee class
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Accountant(
    AdminStaff
):  # Multilevel inheritance, Accountant class inherits from AdminStaff class which inherits from Employee class
    def __init__(self, name, role, salary):
        super().__init__(
            name, role
        )  # Super() function is used to call the constructor of the parent class
        self.salary = salary


accountant1 = Accountant("bob", "accountant", 50000)
print(
    accountant1.name,
    accountant1.role,
    accountant1.salary,
    accountant1.start_time,
    accountant1.end_time,
)


class Teacher:
    def __init__(self, salary):
        self.salary = salary


class Student:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(
    Teacher, Student
):  # Multiple inheritance, TA class inherits from both Teacher and Student classes
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name


# Abstraction: it is the process of hiding the implementation details and only exposing the necessary information to the outside world
class Animal(ABC):
    @abstractmethod
    def sound(
        self,
    ):  # Abstract method, it is a method that is declared but does not have an implementation, it must be implemented by the subclasses
        pass


class Dog(Animal):
    def sound(self):
        print("Woof")


class Cat(Animal):
    def sound(self):
        print("Meow")


labrador = Dog()
labrador.sound()
siamese = Cat()
siamese.sound()


# Polymorphism: it is the ability of an object to take on many forms, it allows us to use a single interface to represent different types of objects
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(4, 6)
shapes = [circle, rectangle]
for shape in shapes:
    print(
        shape.area()
    )  # Function overriding, Python automatically calls the correct area() method


# Duck typing: an object is defined by what it can do (its methods), not by its type or class
class Student:
    def introduce(self):
        print("I am a student")


class Teacher:
    def introduce(self):
        print("I am a teacher")


def greet(person):
    person.introduce()


greet(
    Student()
)  # Greet() doesn't care about the object's type. It only cares that the object has an introduce() method
greet(Teacher())
