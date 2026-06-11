# Q1
string = input("enter a string: ")
reversed_string = string[::-1]
if string == reversed_string:
    print("the string is a palindrome.")
else:   
    print("the string is not a palindrome.")
# or
i = 0
j = len(string) - 1
is_palindrome = True
while i < j:
    if string[i] != string[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("the string is a palindrome.")
else:
    print("the string is not a palindrome.")

# Q2
list = [1, 2, 3, 4, 5]
sum = 0
for num in list:
    sum += num
    average = sum / len(list)
print(f"the average of the list is: {average}")

# Q3
list1 = [1, 2, 7]
list2 = [3, 4, 5]
merged_list = list1 + list2
merged_list.sort()
print(f"the merged and sorted list is: {merged_list}")

# Q4
tuple = (1, 2, 3, 4, 5)
odd_numbers = []
even_numbers = []
for num in tuple:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(f"the odd numbers in the tuple are: {odd_numbers}")
print(f"the even numbers in the tuple are: {even_numbers}")

# Q5
students = {}
while True:
    char = input("enter a character (A, B, C, D, E): ")
    if char == 'A':
        student = input("enter the name of the student: ")
        students[student] = 0 # initialize the marks of the student to 0
    elif char == 'B':
        student = input("enter the name of studemt whose marks you want to update: ")
        if student in students:
            marks = int(input("enter new marks: "))
            students[student] = marks
        else:
            print("student not found")
    elif char == 'C':
        student = input("enter name of student who you want to search: ")
        if student in students:
            print(f"{student} is present in the dictionary with marks {students[student]}")
        else:
            print(f"student not found")
    elif char == 'D':
        print(students)
    elif char == 'E':
        print("exiting program...")
        break
    else:
        print("invalid character entered")

# Q6
words = ["apple", "banana", "cherry", "date", "elderberry"]
word_length = {}
for word in words:
    word_length[word] = len(word)
print(word_length)

# Q7
input_string = input("enter a string: ")
space_count = 0
for char in input_string:
    if char == ' ':
        space_count += 1
print(f"the number of spaces in the string is: {space_count}")
# or
space_count = input_string.count(' ')
print(f"the number of spaces in the string is: {space_count}")

# Q8
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
common = set(list1).intersection(set(list2))
if len(common) == 0:
    print("The lists share no common elements")
else:
    print(f"Common elements: {common}")

# Q9
list1 = [1, 1, 2, 3, 4, 5, 5, 7]
duplicaties = set()
for num in list1:
    if list1.count(num) > 1:
        duplicaties.add(num)
print(duplicaties)
# or
seen = set()
duplicates = set()
for num in list1: 
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(duplicates)

# Q10
# print the unique characters in a string
string = input("enter a string: ")
unique_characters = set()
for char in string:
    unique_characters.add(char)
print(unique_characters)

# print count of unique characters in a string
unique_characters_count = len(unique_characters)
print(f"the number of unique characters in the string is: {unique_characters_count}")





