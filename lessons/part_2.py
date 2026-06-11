# conditional statements
# if 
age = 21
if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")

# if-elif-else
color = input("enter a color: ")
if color == "red":
    print("you like red")
elif color == "blue":
    print("you like blue")
else:
    print("you like some other color")

# user authentication
username = input("enter username: ")
password = input("enter password: ")
if username == "admin" and password == "password123":
    print("login successful")
elif username != "admin":
    print("invalid username")
else:
    print("invalid password")

# odd or even
num = int(input("enter a number: "))
if num == 0:
    print("zero is neither odd nor even")
elif num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# nested if statements
username = input("enter username: ")
password = input("enter password: ")
if username == "admin" and password == "password123":
    print("login successful")
else:
    if username != "admin":
        print("invalid username")
    else:
        print("invalid password")

# match case statement
color = input("enter a color: ")
match color:
    case "green":
        print("go")
    case "yellow":
        print("slow down")
    case "red":
        print("stop")
    case _:
        print("invalid color")

# loops
# while loop
count = 1
while count <= 5:
    print("hello world")
    count += 1

# print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1

# print table of any number
num = int(input("enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# break and continue
# break
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# continue
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

# for loop
string = "hello"
for char in string: # in is the membership operator
    print(char)

# in operator
if "h" in string:
    print("h is in the string")
else: 
    print("h is not in the string")

# print numbers from 1 to 10
for i in range(1, 11): # we use the range function to generate a sequence of numbers
    print(i)

# count number of vowels in a string
string = input("enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"number of vowels in the string: {count}")

# range with step
for i in range(0, 20, 2): # this will print even numbers
    print(i)

# sum of first n natural numbers
n = int(input("enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"sum of first {n} natural numbers: {total}")

# functions
def greet(name):
    print(f"hello {name}")
greet("alice") # alice is the argument passed to the function, it will be assigned to the parameter name
greet("raghav")

# calculate sum of two numbers
def add(a, b = 1): # default value of b is 1
    return a + b
result = add(5, 3)
print(result)

# lambda function
square = lambda x: x ** 2
print(square(5))

# factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # this is a recursive function, it calls itself until it reaches the base case
num = int(input("enter a number: "))
print(f"factorial of {num} is {factorial(num)}")