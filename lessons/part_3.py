# strings
name = "raghav"
print(len(name))
print(name + "gupta") # string concatenation
print(name[3]) # indexing, index starts from 0
for char in name: # iterating through a string
    print(char)
# name[0] = "s" # strings are immutable, we cannot change a character in a string
print(name[1:]) # slicing, it will print from index 1 to the end of the string
print(name[-4:-2]) # it will print from index -4 to index -2 (not inclusive)

# string formatting
# format() method
age = 25
print("my name is {} and I am {} years old".format(name, age))
print("my name is {1} and I am {0} years old".format(age, name)) # index based formatting
print("my name is {name} and I am {age} years old".format(name = name, age = age)) # value based formatting
 
# f-strings
print(f"my name is {name} and I am {age} years old")

# lists
numbers = [1, 2, 3, 4, 5, "six", "7.0"] # lists can contain different data types
print(numbers[2]) # indexing
print(len(numbers)) # length of the list
numbers[2] = 10 # lists are mutable, we can change an element in a list
print(numbers[4:len(numbers)]) # slicing

# list methods
numbers.append(6) # add an element to the end of the list
print(numbers)
numbers.insert(0, 0) # add an element at a specific index
print(numbers)
numbers.remove("six") # remove an element from the list
print(numbers)
numbers.pop() # remove the last element from the list
print(numbers)
numbers.pop(0) # remove an element at a specific index
print(numbers)
numbers.sort() # sort the list in ascending order
print(numbers)
numbers.sort(reverse = True) # sort the list in descending order
print(numbers)
numbers.reverse() # reverse the list
print(numbers)
numbers.clear() # remove all elements from the list
print(numbers)

# loops with lists
numbers = [1, 2, 3, 4, 5]
key = 3
for num in numbers: # linear search
    if num == key:
        print(f"{key} is found at index {numbers.index(num)}")
        break

# tuples
tuple = (1, 2, 3, 4, 5, "six", "7.0") # tuples can contain different data types
single_element_tuple = (1,) # to create a tuple with a single element, we need to add a comma after the element
print(tuple[2]) # indexing
print(len(tuple)) # length of the tuple
# tuple[2] = 10 # tuples are immutable, we cannot change an element in a tuple
print(tuple[4:len(tuple)]) # slicing

# loops with tuples
tuple = (1, 2, 3, 4, 5)
sum = 0
for num in tuple: 
    sum += num
print(f"sum of elements in the tuple: {sum}")

# tuple methods
tuple = (1, 2, 3, 4, 5, "six", "7.0")
print(tuple.index("six")) # find the index of the first occurrence of an element in the tuple
print(tuple.count(3)) # count the number of occurrences of an element in the tuple

# dictionaries
student = {
    "name": "raghav",
    "age": 25,
    "subjects": ["math", "physics", "chemistry"],
    3.14: "pi"
}
print(type(student)) # dictionary is a data type in python
print(student["name"]) # indexing
print(student[3.14]) # we can use different data types as keys in a dictionary
student["age"] = 26 # dictionaries are mutable, we can change the value of a key in a dictionary

# dictionary methods
dict_keys = student.keys() # returns a view object that contains the keys of the dictionary
print(dict_keys)
print(type(dict_keys))
dict_keys_list = list(dict_keys) # we can convert the view object to a list
print(type(dict_keys_list))
dict_values = student.values() # returns a view object that contains the values of the dictionary
print(dict_values)
print(type(dict_values))
dict_items = student.items() # returns a view object that contains the key-value pairs of the dictionary as tuples
print(dict_items)
print(type(dict_items))
print(dict.get("name")) # returns the value of the key, if the key is not found, it returns None
print(dict.get("name", "not found")) # we can also provide a default value to return if the key is not found
student.update({"grade": "A"}) # add a new key-value pair to the dictionary
print(student)

# sets
set1 = {1, 2, 2, 3, 4, 5} # sets do not allow duplicate elements
print(set1)
print(type(set1))
print(len(set1)) # length of the set
empty_set = set() # to create an empty set, we need to use the set() function, we cannot use {} because it creates an empty dictionary
print(empty_set)

# set methods
set1.add(6) # add an element to the set
print(set1)
set1.remove(2) # remove an element from the set, if the element is not found, it raises a KeyError
print(set1)
set1.pop() # remove and return an arbitrary element from the set, if the set is empty, it raises a KeyError
print(set1)
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # returns a new set that contains all the elements from both sets
print(set1.intersection(set2)) # returns a new set that contains only the elements that are present in both sets
set1.clear() # remove all elements from the set
print(set1)

# student enrolments
info = [ 
    ("Alice", "Math"),
    ("Bob", "Physics"),
    ("Charlie", "Chemistry"),
    ("David", "Math"),
    ("Eve", "Physics")
    ("Alice", "Chemistry"),
    ("Eve", "Math"),
    ("Charlie", "Math"),
    ("Bob", "Chemistry")
] # list of tuples, each tuple contains the name of the student and the subject they are enrolled in

# list of unique subjects
subjects = set() # we can use a set to store unique subjects
for tup in info:
    subjects.add(tup[1]) # we can access the subject using index 1 of the tuple
print(subjects)
# or
for name, subject in info: # we can unpack the tuple into name and subject
    subjects.add(subject) # we can access the subject directly
print(subjects)

# students enrolled in Math
math_student = []
for name, subject in info: 
    if subject == "Math":
        math_student.append(name)
print(math_student)

# create dictionary (student, set of subjects)
student_subjects = {}
for name, subject in info:
    if name not in student_subjects:
        student_subjects.update({name: set()}) # if the student is not in the dictionary, we add the student as a key and initialize the value as an empty set
        student_subjects[name].add(subject) # we add the subject to the set of subjects
    else:
        student_subjects[name].add(subject) # if the student is already in the dictionary, we add the subject to the existing set of subjects
print(student_subjects)

