print("Hello world\n", "My name is raghav")

# Variables
name = "raghav"
age = 20
print(name, age)
print("My name is:", name)
print("My age is:", age - 5)

# Data types
isPrime = False
print(type(name))
print(type(age))
print(type(isPrime))

# Sum of two numbers
num1 = 10
num2 = 20
sum = num1 + num2
print(sum)

# Arithmetic operators
print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division
print(num1 % num2)  # Modulus
print(num1**num2)  # Exponentiation

# Comparison operators
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not equal to
print(num1 > num2)  # Greater than
print(num1 < num2)  # Less than
print(num1 >= num2)  # Greater than or equal to
print(num1 <= num2)  # Less than or equal to

# Assignment operators
num1 += num2  # num1 = num1 + num2
print(num1)
num1 -= num2  # num1 = num1 - num2
print(num1)
num1 *= num2  # num1 = num1 * num2
print(num1)
num1 /= num2  # num1 = num1 / num2
print(num1)
num1 %= num2  # num1 = num1 % num2
print(num1)
num1 **= num2  # num1 = num1 ** num2
print(num1)

# Logical operators
print(num1 > num2 and num1 < 100)  # Logical AND
print(num1 > num2 or num1 < 100)  # Logical OR
print(not (num1 > num2))  # Logical NOT

# Type casting
num1 = "10"
num2 = "20"
print(int(num1) + int(num2))  # String to integer
ans = int(5 + 10.5)  # Float to integer
print(ans)

# Taking user input
name = input("Enter your name: ")
print(name)
a = input("Enter a number: ")
b = input("Enter another number: ")
print(a + b)  # Concatenates the two strings.
print(int(a) + int(b))  # Adds the two numbers.

# Calculate average of three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("The average is:", average)
