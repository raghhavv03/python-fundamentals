# Strings
name = "raghav"
print(len(name))
print(name + "gupta")  # String concatenation.
print(name[3])  # Indexing (0-based).
for char in name:  # Iterating through a string.
    print(char)
# name[0] = "s" # Strings are immutable.
print(name[1:])  # Slicing from index 1 to end.
print(name[-4:-2])  # Slicing from index -4 to -2 (exclusive).

# String formatting
# Format() method
age = 25
print("My name is {} and I am {} years old".format(name, age))
print(
    "My name is {1} and I am {0} years old".format(age, name)
)  # Index-based formatting
print(
    "My name is {name} and I am {age} years old".format(name=name, age=age)
)  # Value-based formatting

# F-strings
print(f"My name is {name} and I am {age} years old")

# Lists
numbers = [1, 2, 3, 4, 5, "six", "7.0"]  # Lists can contain different data types
print(numbers[2])  # Indexing
print(len(numbers))  # Length of the list
numbers[2] = 10  # Lists are mutable, we can change an element in a list
print(numbers[4 : len(numbers)])  # Slicing

# List methods
numbers.append(6)  # Add an element to the end of the list
print(numbers)
numbers.insert(0, 0)  # Add an element at a specific index
print(numbers)
numbers.remove("six")  # Remove an element from the list
print(numbers)
numbers.pop()  # Remove the last element from the list
print(numbers)
numbers.pop(0)  # Remove an element at a specific index
print(numbers)
numbers.sort()  # Sort the list in ascending order
print(numbers)
numbers.sort(reverse=True)  # Sort the list in descending order
print(numbers)
numbers.reverse()  # Reverse the list
print(numbers)
numbers.clear()  # Remove all elements from the list
print(numbers)

# Loops with lists
numbers = [1, 2, 3, 4, 5]
key = 3
for num in numbers:  # Linear search
    if num == key:
        print(f"{key} is found at index {numbers.index(num)}")
        break

# Tuples
tuple = (1, 2, 3, 4, 5, "six", "7.0")  # Tuples can contain different data types
single_element_tuple = (1,)  # Single-element tuple requires a trailing comma.
print(tuple[2])  # Indexing
print(len(tuple))  # Length of the tuple
# tuple[2] = 10 # Tuples are immutable, we cannot change an element in a tuple
print(tuple[4 : len(tuple)])  # Slicing

# Loops with tuples
tuple = (1, 2, 3, 4, 5)
sum = 0
for num in tuple:
    sum += num
print(f"Sum of elements in the tuple: {sum}")

# Tuple methods
tuple = (1, 2, 3, 4, 5, "six", "7.0")
print(
    tuple.index("six")
)  # Find the index of the first occurrence of an element in the tuple
print(tuple.count(3))  # Count the number of occurrences of an element in the tuple

# Dictionaries
student = {
    "name": "raghav",
    "age": 25,
    "subjects": ["math", "physics", "chemistry"],
    3.14: "pi",
}
print(type(student))  # Dictionary is a data type in Python
print(student["name"])  # Indexing
print(student[3.14])  # We can use different data types as keys in a dictionary
student["age"] = (
    26  # Dictionaries are mutable, we can change the value of a key in a dictionary
)

# Dictionary methods
dict_keys = (
    student.keys()
)  # Returns a view object that contains the keys of the dictionary
print(dict_keys)
print(type(dict_keys))
dict_keys_list = list(dict_keys)  # We can convert the view object to a list
print(type(dict_keys_list))
dict_values = (
    student.values()
)  # Returns a view object that contains the values of the dictionary
print(dict_values)
print(type(dict_values))
dict_items = (
    student.items()
)  # Returns a view object that contains the key-value pairs of the dictionary as tuples
print(dict_items)
print(type(dict_items))
print(
    dict.get("name")
)  # Returns the value of the key, if the key is not found, it returns None
print(
    dict.get("name", "not found")
)  # We can also provide a default value to return if the key is not found
student.update({"grade": "A"})  # Add a new key-value pair to the dictionary
print(student)

# Sets
set1 = {1, 2, 2, 3, 4, 5}  # Sets do not allow duplicate elements
print(set1)
print(type(set1))
print(len(set1))  # Length of the set
empty_set = set()  # Empty set requires set(); {} creates an empty dictionary.
print(empty_set)

# Set methods
set1.add(6)  # Add an element to the set
print(set1)
set1.remove(
    2
)  # Remove an element from the set, if the element is not found, it raises a KeyError
print(set1)
set1.pop()  # Remove and return an arbitrary element from the set, if the set is empty, it raises a KeyError
print(set1)
set2 = {4, 5, 6, 7, 8}
print(
    set1.union(set2)
)  # Returns a new set that contains all the elements from both sets
print(
    set1.intersection(set2)
)  # Returns a new set that contains only the elements that are present in both sets
set1.clear()  # Remove all elements from the set
print(set1)

# Student enrolments
info = [
    ("Alice", "Math"),
    ("Bob", "Physics"),
    ("Charlie", "Chemistry"),
    ("David", "Math"),
    ("Eve", "Physics"),
    ("Alice", "Chemistry"),
    ("Eve", "Math"),
    ("Charlie", "Math"),
    ("Bob", "Chemistry"),
]  # List of tuples (student, subject).

# List of unique subjects
subjects = set()  # We can use a set to store unique subjects
for tup in info:
    subjects.add(tup[1])  # We can access the subject using index 1 of the tuple
print(subjects)
# Or
for name, subject in info:  # We can unpack the tuple into name and subject
    subjects.add(subject)  # We can access the subject directly
print(subjects)

# Students enrolled in Math
math_student = []
for name, subject in info:
    if subject == "Math":
        math_student.append(name)
print(math_student)

# Create dictionary (student, set of subjects)
student_subjects = {}
for name, subject in info:
    if name not in student_subjects:
        student_subjects.update(
            {name: set()}
        )  # If the student is not in the dictionary, we add the student as a key and initialize the value as an empty set
        student_subjects[name].add(subject)  # We add the subject to the set of subjects
    else:
        student_subjects[name].add(
            subject
        )  # If the student is already in the dictionary, we add the subject to the existing set of subjects
print(student_subjects)
