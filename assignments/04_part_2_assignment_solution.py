# Q1
salary = float(input("Enter your salary: " ))
if salary < 30000:
    print("your final tax rate is 5%")
elif salary >= 30000 and salary <= 70000:
    print("your final tax rate is 15%")
else:
    print("your final tax rate is 25%")

#Q2
a = int(input("enter first number: "))
b = int(input("enter second number: "))
for i in range(a, b+1):
    if i % 2 == 0:
        print(i)

# Q3
n = int(input("enter a number: "))
digits = []
while n > 0:
    digit = n % 10
    digits.append(digit)
    n = n // 10 # takes the floor division to remove the last digit
for digit in reversed(digits):
    print(digit)

# Q4
n = input("enter a number: ")
count = 0
for digit in n:
    count += 1
print(f"number of digits in the number: {count}")

# Q5
n = int(input("enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum +=digit
    n = n // 10
print(f"sum of digits in the number: {sum}")

# Q6
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Q7
while True:
    num = input("enter a number: ")
    if num == "quit":
        break
    else:
        num = float(num)
        if num > 0:
            print("positive")
        elif num < 0:
            print("negative")
        else:
            print("zero")

# Q8
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "division by zero is not allowed"
    else:
        return "invalid operator"
a = float(input("enter first number: "))
b = float(input("enter second number: "))
operator = input("enter operator (+, -, *, /): ")
result = calculator(a, b, operator)
print(f"result: {result}")

# Q9
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1): # we only need to check up to the square root of n
        if n % i == 0:
            return False
    return True
n = int(input("enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

# Q10
secret_number = 7
while True:
    guess = int(input("guess the secret number: "))
    if guess < secret_number:
        print("too low")
    elif guess > secret_number:
        print("too high")
    else:
        print("correct")
        break
