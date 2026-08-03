# Conditional statements
# If
age = 21
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-elif-else
color = input("Enter a color: ")
if color == "red":
    print("You like red")
elif color == "blue":
    print("You like blue")
else:
    print("You like some other color")

# User authentication
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Login successful")
elif username != "admin":
    print("Invalid username")
else:
    print("Invalid password")

# Odd or even
num = int(input("Enter a number: "))
if num == 0:
    print("Zero is neither odd nor even")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Nested if statements
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Login successful")
else:
    if username != "admin":
        print("Invalid username")
    else:
        print("Invalid password")

# Match case statement
color = input("Enter a color: ")
match color:
    case "green":
        print("Go")
    case "yellow":
        print("Slow down")
    case "red":
        print("Stop")
    case _:
        print("Invalid color")

# Loops
# While loop
count = 1
while count <= 5:
    print("Hello world")
    count += 1

# Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1

# Print table of any number
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Break and continue
# Break
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# Continue
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

# For loop
string = "hello"
for char in string:  # 'in' is the membership operator.
    print(char)

# In operator
if "h" in string:
    print("H is in the string")
else:
    print("H is not in the string")

# Print numbers from 1 to 10
for i in range(1, 11):  # Generates a sequence of numbers from 1 to 10.
    print(i)

# Count number of vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")

# Range with step
for i in range(0, 20, 2):  # Prints even numbers.
    print(i)

# Sum of first n natural numbers
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of first {n} natural numbers: {total}")


# Functions
def greet(name):
    print(f"Hello {name}")


greet("alice")  # "alice" is the argument passed to the function.
greet("raghav")


# Calculate sum of two numbers
def add(a, b=1):  # Default value of b is 1.
    return a + b


result = add(5, 3)
print(result)

# Lambda function
square = lambda x: x**2
print(square(5))


# Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call until reaching the base case.


num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
