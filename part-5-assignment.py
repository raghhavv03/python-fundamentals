# Q1
with open("python-fundamentals/names.txt", "w") as f:
    for i in range(0, 5):
        name = input("enter a name: ")
        f.write(name + "\n")

with open("python-fundamentals/names.txt", "r") as f:
    names = f.readlines()
    for name in names:
        print(name)

# Q2
with open("python-fundamentals/logs.txt", "a") as f:
    f.write("program run successfully\n")

with open("python-fundamentals/logs.txt", "r") as f:
    logs = f.readlines()
    for log in logs:
        print(log)

# Q3
list1 = [5, 10, 15, 20, 25]
list1 = [i for i in list1 if i > 15]
print(list1)

# Q4
import json

cities = {
    "delhi": 1000000,
    "mumbai": 2000000,
    "chennai": 3000000,
    "kolkata": 4000000,
    "bengaluru": 5000000
}

with open("python-fundamentals/cities.json", "w") as f:
    json.dump(cities, f, indent = 4, sort_keys = True)

with open("python-fundamentals/cities.json", "r") as f:
    cities = json.load(f)
    print(cities)

new_city = input("enter a new city: ")
new_population = int(input("enter the population of the city: "))
cities[new_city] = new_population

with open("python-fundamentals/cities.json", "w") as f:
    json.dump(cities, f, indent = 4, sort_keys = True)
 
# Q5
try: 
    with open("python-fundamentals/data.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("file not found")


