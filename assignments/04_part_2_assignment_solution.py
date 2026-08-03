# Q1
salary = float(input("Enter your salary: "))
if salary < 30000:
    print("Your final tax rate is 5%")
elif salary >= 30000 and salary <= 70000:
    print("Your final tax rate is 15%")
else:
    print("Your final tax rate is 25%")

# Q2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)

# Q3
n = int(input("Enter a number: "))
digits = []
while n > 0:
    digit = n % 10
    digits.append(digit)
    n = n // 10  # Uses floor division to remove the last digit.
for digit in reversed(digits):
    print(digit)

# Q4
n = input("Enter a number: ")
count = 0
for digit in n:
    count += 1
print(f"Number of digits in the number: {count}")

# Q5
n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
print(f"Sum of digits in the number: {sum}")

# Q6
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Q7
while True:
    num = input("Enter a number: ")
    if num == "quit":
        break
    else:
        num = float(num)
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")


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
            return "Division by zero is not allowed."
    else:
        return "Invalid operator."


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
result = calculator(a, b, operator)
print(f"Result: {result}")


# Q9
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to the square root of n.
        if n % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

# Q10
secret_number = 7
while True:
    guess = int(input("Guess the secret number: "))
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Correct.")
        break
