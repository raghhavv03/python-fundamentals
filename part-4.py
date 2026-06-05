# oops
# classes are blueprints for creating objects. They define the properties and behaviors of the objects
# an object is an instance of a class. It is created using the class and has its own unique identity and state
class Student: 
    subject = "python"
    college = "abc university"

student1 = Student() # creating an object of the Student class
student2 = Student() 
print(student1) # the object is stored in memory and has a unique id
print(student2) 
print(student1.subject, student1.college) # we can access the properties of the object using dot notation

list1 = [1, 2, 3, 4, 5]
print(type(list)) # the type of the object is list. python has built-in classes for different data types like int, float, str, list, dict, set, etc. we can also create our own classes
set1 = set() # we can create an empty set using set method of class set

# constructors
class Student:
    college = "abc university" 

    def __init__(self, name, age): # self keyword is used to refer to the current object. it is used to access the properties and methods of the object. it is a convention to use self as the name of the first parameter of the constructor, but we can use any name we want
        self.name = name # we can use self to create properties of the object and assign values to them. the properties of the object are defined in the constructor and are initialized when the object is created
        self.age = age
        print("constructor called") # the constructor is a special method that is called when an object is created. it is used to initialize the properties of the object

student1 = Student("alice", 20) # creating an object of the Student class and passing arguments to the constructor
student2 = Student("bob", 22)
# in python we should not create multiple constructors in a class, we can use default values for the parameters of the constructor to achieve the same functionality

# attributes
# class attributes are shared by all objects of the class, they are defined outside the constructor and are accessed using the class name or the object name
# instance attributes are unique to each object, they are defined in the constructor and are accessed using the object name
print(Student.college) # we can access the class attribute using the class name
print(student1.name) # we can access the instance attribute using the object name
# print(Student.name) # we cannot access the instance attribute using the class name, it will raise an AttributeError

# methods
class Laptop:
    storage_type = "SSD" 

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod # decorator to define a class method
    def get_storage_type(cls): # class method, it is a method that is defined in the class and is called using the class name
        print(f"the storage type of the laptop is {cls.storage_type}.") 

    def laptop_info(self): # instance method, it is a method that is defined in the class and is called using the object
        print(f"the laptop has {self.ram} gb of ram and {self.storage} gb of {self.storage_type}.")
    
    @staticmethod # decorator to define a static method
    def discount(price, percentage): # static method, it is a method that is defined in the class and is called using the class name. it does not have access to the class attributes or instance attributes
        discounted_price = price - (price * percentage / 100)
        print(f"the discounted price is {discounted_price}.")

laptop1 = Laptop(16, 512)
laptop2 = Laptop(8, 256)
laptop1.laptop_info() 
Laptop.get_storage_type() # we can call the class method using the class name
laptop1.get_storage_type() # we can also call the class method using the object name
Laptop.discount(1000, 10) # we can also call the static method using the class name
laptop1.discount(1000, 10) # we can call the static method using the object name

# create an online store for products
class Product:
    count = 0 # class attribute to keep track of the number of products created
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1 # increment the count of products created

    def product_info(self):
        print(f"the product name is {self.name} and the price is {self.price}.")
    
    @classmethod
    def product_count(cls):
        print(f"the number of products created is {Product.count}.")
    
    @staticmethod
    def calculate_discount(price, percentage):
        discounted_price = price - (price * percentage / 100)
        print(f"the discounted price is {discounted_price}.")

p1 = Product("laptop", 1000)
p2 = Product("phone", 500)
p3 = Product("tablet", 300)
p1.product_info()
Product.product_count() 
p1.product_count()
Product.calculate_discount(1000, 10) 
p1.calculate_discount(p1.price, 10) # we can also dyanmically pass the price of the product to the static method

# oops pillars
# encapsulation: it is the process of hiding the internal details of an object and only exposing the necessary information to the outside world
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # private attribute
    
    def set_balance(self, balance): # setter method to modify the private attribute
        if balance < 0:
            print("balance cannot be negative")
        else:
            self.__balance = balance
    
    def get_balance(self): # getter method to access the private attribute
        return self.__balance

account1 = BankAccount("alice", 1000)
print(account1.get_balance()) # we can access the private attribute using the getter method
account1.set_balance(1500) # we can modify the private attribute using the setter method
print(account1.name, account1.BankAccount__balance) # we cannot access the private attribute directly, it will raise an AttributeError, but we can access it using name mangling, it is not recommended to do so

# inheritance: it is the process of creating a new class that is a modified version of an existing class
class Employee:
    start_time = "9 am"
    end_time = "5 pm"

    def change_shift(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

class Teacher(Employee): # Teacher class inherits the properties of the Employee class, it is called a child class or subclass, Employee is the parent class or superclass
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

t1 = Teacher("alice", "math")
print(t1.name, t1.subject, t1.start_time, t1.end_time) # the Teacher class inherits the properties of the Employee class, we can access the class attributes of the Employee class using the object of the Teacher class
t1.change_shift("8 am", "4 pm") # we can also call the method of the Employee class using the object of the Teacher class

# types of inheritance
class Employee:
    start_time = "9 am"
    end_time = "5 pm"

class AdminStaff(Employee): # single inheritance, AdminStaff class inherits from Employee class
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Accountant(AdminStaff): # multilevel inheritance, Accountant class inherits from AdminStaff class which inherits from Employee class
    def __init__(self, name, role, salary):
        super().__init__(name, role) # super() function is used to call the constructor of the parent class
        self.salary = salary

accountant1 = Accountant("bob", "accountant", 50000)
print(accountant1.name, accountant1.role, accountant1.salary, accountant1.start_time, accountant1.end_time)

class Teacher:
    def __init__(self, salary):
        self.salary = salary
    
class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student): # multiple inheritance, TA class inherits from both Teacher and Student classes
    def __init__(self, salary, gpa, name):
        super().__init__(salary) 
        Student.__init__(self, gpa)
        self.name = name

# abstraction: it is the process of hiding the implementation details and only exposing the necessary information to the outside world
from abc import ABC, abstractmethod # ABC is the abstract base class, it is a class that cannot be instantiated and is used as a base class for other classes. abstractmethod is a decorator

class Animal(ABC):
    @abstractmethod
    def sound(self): # abstract method, it is a method that is declared but does not have an implementation, it must be implemented by the subclasses
        pass

class Dog(Animal):
    def sound(self):
        print("woof")

class Cat(Animal):
    def sound(self):
        print("meow")

labrador = Dog()
labrador.sound()
siamese = Cat()
siamese.sound()

# polymorphism: it is the ability of an object to take on many forms, it allows us to use a single interface to represent different types of objects
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
    print(shape.area()) # function overriding, python automatically calls the correct area() method

# duck typing: an object is defined by what it can do (its methods), not by its type or class
class Student:
    def introduce(self):
        print("i am a student")

class Teacher:
    def introduce(self):
        print("i am a teacher")

def greet(person):
    person.introduce()

greet(Student()) # greet() doesn't care about the object's type. it only cares that the object has an introduce() method
greet(Teacher())







