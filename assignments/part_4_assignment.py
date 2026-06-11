# Q1
class BankAccount:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"amount deposited successfully. new balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance.")
        else:
            self.balance -= amount
            print(f"amount withdrawn successfully. new balance is {self.balance}.")
    
    def check_balance(self):
        print(f"the current balance is {self.balance}.")

account1 = BankAccount("1234567890", "raghav", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

# Q2
class Book:
    def __init__(self, title, author, review_list):
        self.title = title
        self.author = author
        self.review_list = review_list
    
    def add_review(self, review):
        self.review_list.append(review)
        print("review added successfully.")
    
    def count_reviews(self):
        print(f"the number of reviews for the book is {len(self.review_list)}.")
    
    def display_reviews(self):
        print("reviews for the book:")
        for review in self.review_list:
            print(review)
    
book1 = Book("the alchemist", "paulo coelho", [])
book1.add_review("a great book with a powerful message.")
book1.add_review("a must read for everyone.")
book1.count_reviews()
book1.display_reviews()

# Q3
class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)
    
    def set_name(self, name):
        if name == "":
            print("name cannot be empty.")
        else:
            self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("roll number must be between 1 and 100")

    def get_roll_no(self):
        return self.__roll_no
    
    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            print("marks should be between 0 and 100.")
        else:
            self.__marks = marks

    def get_marks(self):
        return self.__marks
    
student1 = Student("raghav", "12345", 85)
print(student1.get_name())
print(student1.get_roll_no())
print(student1.get_marks())

# Q4
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
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

c1 = Circle(5)
r1 = Rectangle(4, 6)
t1 = Triangle(4, 5)
print(f"area of the circle is: {c1.area()}")
print(f"area of the rectangle is: {r1.area()}")
print(f"area of the triangle is: {t1.area()}")

# Q5
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

car1 = Car("toyota", "camry", 5)
bike1 = Bike("honda", "cbr", 1000)
print(f"car brand: {car1.brand}, model: {car1.model}, seats: {car1.seats}")
print(f"bike brand: {bike1.brand}, model: {bike1.model}, engine cc: {bike1.engine_cc}")

# Q6
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend
    
    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_salary(self):
        return self.salary
    
class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

intern1 = Intern(1000)
full_time_employee1 = FullTimeEmployee(50000)
contract_employee1 = ContractEmployee(20, 160)
print(f"intern salary: {intern1.calculate_salary()}")
print(f"full time employee salary: {full_time_employee1.calculate_salary()}")
print(f"contract employee salary: {contract_employee1.calculate_salary()}")

# Q7
class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address
    
person1 = Person("alice", 30, "123 main st")
person2 = Person("bob", 25)
person3 = Person("charlie")
print(f"person1: name: {person1.name}, age: {person1.age}, address: {person1.address}")
print(f"person2: name: {person2.name}, age: {person2.age}, address: {person2.address}")
print(f"person3: name: {person3.name}, age: {person3.age}, address: {person3.address}")

# Q8
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

player1 = Player("alice", 5)
player2 = Player("bob", 10)
print(f"number of players: {Player.player_count}")

# Q9
class Herbivore:
    def eat_grass(self):
        print(f"{self.name} is eating grass.")

class Carnivore:
    def eat_meat(self):
        print(f"{self.name} is eating meat.")

class Omnivore:
    def eat_both(self):
        print(f"{self.name} is eating both grass and meat.")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is a bear.")

bear1 = Bear("baloo")
bear1.eat_grass()
bear1.eat_meat()
bear1.eat_both()

# Q10
class Message:
    message_counter = 1
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1
    
    def __str__(self): # to print the message in a readable format
        return f"({self.id}) {self.sender.name}: {self.content}"
    

class User:
    def __init__(self, name):
        self.name = name
        self.chatroom = None
    
    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.name} is already in a chatroom.")
        else:
            self.chatroom = chatroom
            chatroom.add_user(self)
            print(f"{self.name} has joined the chatroom.")
        
    def leave_chatroom(self):
        if self.chatroom:
            self.chatroom.remove_user(self)
            print(f"{self.name} has left the chatroom.")
            self.chatroom = None
        else:
            print(f"{self.name} is not in a chatroom.")
    
    def send_message(self, message):
        if self.chatroom:
            self.chatroom.broadcast_message(self, message)
        else:
            print(f"{self.name} is not in a chatroom. cannot send message.")

class ChatRoom:    
    def __init__(self, name):
        self.name = name
        self.users =[]
        self.messages = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)
    
    def broadcast_message(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message) # python automatically calls the __str__ method of the message class to print the message in a readable format
    
    def show_chat_history(self):
        print(f"chat history for {self.name}:")
        for message in self.messages:
            print(message) 
        print() # to add a new line after the chat history

if __name__ == "__main__": # to test the chat room functionality
    room = ChatRoom("general")
    user1 = User("alice")
    user2 = User("bob")
    user3 = User("charlie")
    user1.join_chatroom(room)
    user2.join_chatroom(room)
    user1.send_message("hello everyone!")
    user2.send_message("hi alice!")
    user3.join_chatroom(room)
    user3.send_message("hey guys, what's up?")
    room.show_chat_history()
    user1.leave_chatroom()
    user2.leave_chatroom()
    user3.leave_chatroom()

