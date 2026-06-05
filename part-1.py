print("hello world\n", "my name is raghav")

# variables
name = "raghav"
age = 20
print(name, age)
print("my name is:", name)
print("my age is:", age - 5)

# data types
isPrime = False
print(type(name))
print(type(age))
print(type(isPrime))

# sum of two numbers
num1 = 10
num2 = 20
sum = num1 + num2
print(sum)

# arithmetic operators
print(num1 + num2) # addition
print(num1 - num2) # subtraction
print(num1 * num2) # multiplication
print(num1 / num2) # division
print(num1 % num2) # modulus
print(num1 ** num2) # exponentiation

# comparison operators
print(num1 == num2) # equal to
print(num1 != num2) # not equal to
print(num1 > num2) # greater than
print(num1 < num2) # less than
print(num1 >= num2) # greater than or equal to
print(num1 <= num2) # less than or equal to

# assignment operators
num1 += num2 # num1 = num1 + num2
print(num1)
num1 -= num2 # num1 = num1 - num2
print(num1)
num1 *= num2 # num1 = num1 * num2
print(num1)
num1 /= num2 # num1 = num1 / num2
print(num1)     
num1 %= num2 # num1 = num1 % num2
print(num1)     
num1 **= num2 # num1 = num1 ** num2
print(num1)     

# logical operators
print(num1 > num2 and num1 < 100) # logical AND
print(num1 > num2 or num1 < 100) # logical OR
print(not(num1 > num2)) # logical NOT

# type casting
num1 = "10"
num2 = "20"
print(int(num1) + int(num2)) # string to integer
ans = int(5 + 10.5) # float to integer
print(ans)

# taking user input
name = input("enter your name: ")
print(name)
a = input("enter a number: ")
b = input("enter another number: ")
print(a + b) # this will concatenate the two strings
print(int(a) + int(b)) # this will add the two numbers

# calculate average of three numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
average = (num1 + num2 + num3) / 3
print("the average is:", average)