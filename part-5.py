# file operations
f = open("python-fundamentals/sample1.txt", "r") # open the file in read mode
print(f.readline()) # read the file line by line and pointer moves to the next line
print(f.read()) # read the file
f.close() # close the file

f = open("python-fundamentals/sample1.txt", "w") # open the file in write mode and overwrite the file
f.write("hello world\n") # write to the file
f.close() # close the file

f = open("python-fundamentals/sample1.txt", "a") # open the file in append mode and add to the end of the file
f.write("appending to the file\n") # write to the file
f.close() # close the file

f = open("python-fundamentals/sample2.txt", "x") # create a new file if it doesn't exist
f.write("hello world\n") # write to the file
f.close() # close the file

f = open("python-fundamentals/sample3.txt", "r+") # open the file in read and write mode
f.write("123\n") # write to the file
print(f.read()) # read the file
f.close() 

f = open("python-fundamentals/sample3.txt", "a+") # open the file in append and read mode
f.write("123\n") # write to the file
print(f.read()) # read the file
f.close()

f = open("python-fundamentals/sample3.txt", "w+") # open the file in write and read mode
f.write("hello world\n") # write to the file
print(f.read()) # read the file
f.close() 

# with keyword
# files are automatically closed when the block is exited
with open("python-fundamentals/sample1.txt", "r") as f:
    print(f.readline()) 
    data = f.read()
    print(len(data))

# delete a file
import os

os.remove("python-fundamentals/sample1.txt")
print("file deleted")

# word search
data = True
count = 1
with open("python-fundamentals/word-search.txt", "r") as f:
    while data:
        data = f.readline()
        if "python" in data.lower():
            print(f"python is found at line {count}")
            break
        count += 1

# exception handling
try: # try block to test a block of code for errors
    x = int(input("enter a number: "))
    ans = 100 / x

except ZeroDivisionError: # exception handler for zero division error
    print("division by zero is not allowed")

except ValueError: # exception handler for value error
    print("invalid input")

else: # else block to execute if no error is raised
    print(f'answer is {ans}')

finally: # finally block to execute after try and except blocks
    print("thank you for using the calculator")

# list comprehension
# list comprehension is a more concise way to create a new list
list1 = []
for i in range (1, 11):
    if i % 2 == 0:
        list1.append(i * i)
print(list1)

# using list comprehension
list2 = [i * i for i in range (1, 11) if i % 2 == 0]
print(list2)

list3 = [-1, 3, 7, -6, 5]
list3 = [0 if i < 0 else i for i in list3] # replace negative numbers with 0
print(list3)

list4 = ["hello", "world", "python", "java", "c++"]
list4 = [word.upper() for word in list4] # convert all words to uppercase
print(list4)

# json module
import json 

json_str = '{"name": "raghav", "isStudent": true, "age": 20, "subjects": ["math", "physics", "chemistry"], "marks": {"math": 90, "physics": 80, "chemistry": 70}}' # this is a json string
print(type(json_str)) # json string is a string

# convert json string to python object
py_obj = json.loads(json_str) # loads method is used to load the json string into a python object
print(type(py_obj)) # python object is a dictionary
print(py_obj)

# convert python object to json string
json_str = json.dumps(py_obj) # dumps method is used to convert the python object into a json string
print(type(json_str)) 
print(json_str)

# files
with open("python-fundamentals/data.json", "r") as f:
    py_obj = json.load(f) # load method is used to load the json data from a file into a python object
    print(type(py_obj))
    print(py_obj)

# write json data to a file
with open("python-fundamentals/data.json", "w") as f:
    json.dump(py_obj, f, indent = 4, ) # dump method is used to write the json data to a file, indent is used to format the json data








 



    
    
