# Q1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old")

# Q2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2, num1 - num2, num1 * num2, num1 / num2)

# Q3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num1 = float(num1)
num2 = float(num2)
average = (num1 + num2 + num3) / 3
print("The average is", average)

# Q4
num = input("Enter a number: ")
num_int = int(num)
num_float = float(num)
num_str = str(num)
print("Integer:", num_int, "type:", type(num_int))
print("Float:", num_float, "type:", type(num_float))
print("String:", num_str, "type:", type(num_str))

# Q5
x = 10 + 3 * 2**2
print(x)

# Q6
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
temp = a
a = b
b = temp
# a, b = b, a # This is a more Pythonic way to swap two variables.
print("A:", a, "B:", b)

# Q7
cel_temp = float(input("Enter temperature in Celsius: "))
fah_temp = (cel_temp * 9 / 5) + 32
print("Temperature in Fahrenheit:", fah_temp)

# Q8
rad = float(input("Enter radius of the circle: "))
area = 3.14 * rad**2
print("Area of the circle:", area)

# Q9
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple interest:", simple_interest)

# Q10
num = float(input("Enter a decimal number: "))
integer_part = int(num)
decimal_part = num - integer_part
print("Integer part:", integer_part)
print("Decimal part:", decimal_part)
