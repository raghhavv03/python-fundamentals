import json
import os


# File operations
f = open("data/sample_1.txt", "r")  # Open the file in read mode
print(f.readline())  # Read the file line by line and pointer moves to the next line
print(f.read())  # Read the file
f.close()  # Close the file

f = open("data/sample_1.txt", "w")  # Open the file in write mode and overwrite the file
f.write("hello world\n")  # Write to the file
f.close()  # Close the file

f = open(
    "data/sample_1.txt", "a"
)  # Open the file in append mode and add to the end of the file
f.write("appending to the file\n")  # Write to the file
f.close()  # Close the file

f = open("data/sample_2.txt", "x")  # Create a new file if it doesn't exist
f.write("hello world\n")  # Write to the file
f.close()  # Close the file

f = open("data/sample_3.txt", "r+")  # Open the file in read and write mode
f.write("123\n")  # Write to the file
print(f.read())  # Read the file
f.close()

f = open("data/sample_3.txt", "a+")  # Open the file in append and read mode
f.write("123\n")  # Write to the file
print(f.read())  # Read the file
f.close()

f = open("data/sample_3.txt", "w+")  # Open the file in write and read mode
f.write("hello world\n")  # Write to the file
print(f.read())  # Read the file
f.close()

# With keyword
# Files are automatically closed when the block is exited
with open("data/sample_1.txt", "r") as f:
    print(f.readline())
    data = f.read()
    print(len(data))

# Delete a file
os.remove("data/sample_1.txt")
print("File deleted")

# Word search
data = True
count = 1
with open("data/word_search.txt", "r") as f:
    while data:
        data = f.readline()
        if "python" in data.lower():
            print(f"Python is found at line {count}")
            break
        count += 1

# Exception handling
try:  # Try block to test a block of code for errors
    x = int(input("Enter a number: "))
    ans = 100 / x

except ZeroDivisionError:  # Exception handler for zero division error
    print("Division by zero is not allowed.")

except ValueError:  # Exception handler for value error
    print("Invalid input.")

else:  # Else block to execute if no error is raised
    print(f"Answer is {ans}")

finally:  # Finally block to execute after try and except blocks
    print("Thank you for using the calculator.")

# List comprehension
# List comprehension is a more concise way to create a new list
list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i * i)
print(list1)

# Using list comprehension
list2 = [i * i for i in range(1, 11) if i % 2 == 0]
print(list2)

list3 = [-1, 3, 7, -6, 5]
list3 = [0 if i < 0 else i for i in list3]  # Replace negative numbers with 0
print(list3)

list4 = ["hello", "world", "python", "java", "c++"]
list4 = [word.upper() for word in list4]  # Convert all words to uppercase
print(list4)

# JSON module
json_str = '{"name": "raghav", "isStudent": true, "age": 20, "subjects": ["math", "physics", "chemistry"], "marks": {"math": 90, "physics": 80, "chemistry": 70}}'  # This is a JSON string
print(type(json_str))  # JSON string is a string

# Convert JSON string to Python object
py_obj = json.loads(
    json_str
)  # Loads method is used to load the JSON string into a Python object
print(type(py_obj))  # Python object is a dictionary
print(py_obj)

# Convert Python object to JSON string
json_str = json.dumps(
    py_obj
)  # Dumps method is used to convert the Python object into a JSON string
print(type(json_str))
print(json_str)

# Files
with open("data/data.json", "r") as f:
    py_obj = json.load(
        f
    )  # Load method is used to load the JSON data from a file into a Python object
    print(type(py_obj))
    print(py_obj)

# Write JSON data to a file
with open("data/data.json", "w") as f:
    json.dump(
        py_obj,
        f,
        indent=4,
    )  # Dump method is used to write the JSON data to a file, indent is used to format the JSON data
