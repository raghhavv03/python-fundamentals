# Q1
name = input("enter your name: ")
age = int(input("enter your age: "))
print("hello", name, "you are", age, "years old")

#Q2
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print(num1 + num2, num1 - num2, num1 * num2, num1 / num2)

# Q3
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = float(input("enter third number: "))
num1 = float(num1)
num2 = float(num2)
average = (num1 + num2 + num3) / 3
print("the average is", average)

# Q4
num = input("enter a number: ")
num_int = int(num)
num_float = float(num)
num_str = str(num)
print("integer:", num_int, "type:", type(num_int))
print("float:", num_float, "type:", type(num_float))
print("string:", num_str, "type:", type(num_str))

# Q5 
x = 10 + 3 * 2 ** 2
print(x)

# Q6 
a = int(input("enter a number: "))
b = int(input("enter another number: "))
temp = a
a = b
b = temp
# a, b = b, a # this is a more pythonic way to swap two variables
print("a:", a, "b:", b)

# Q7
cel_temp = float(input("enter temperature in celsius: "))
fah_temp = (cel_temp * 9/5) + 32
print("temperature in fahrenheit:", fah_temp)

# Q8
rad = float(input("enter radius of the circle: "))
area = 3.14 * rad ** 2
print("area of the circle:", area)

# Q9 
principal = float(input("enter principal amount: "))
rate = float(input("enter rate of interest: "))
time = float(input("enter time in years: "))
simple_interest = (principal * rate * time) / 100
print("simple interest:", simple_interest)

# Q10
num = float(input("enter a decimal number: "))
integer_part = int(num)
decimal_part = num - integer_part
print("integer part:", integer_part)
print("decimal part:", decimal_part)

