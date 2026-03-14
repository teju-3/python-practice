# The Basic Structure of a for Loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)

#  Using range() with for Loops
for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

#  Looping Over Strings
name = "Karnataka"
for letter in name:
    print(letter)

# Nested for Loops
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # To print an empty line after each table

# Using break in a for Loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        print(f"Found {city}!")
        break
    print(city)

# Using continue in a for Loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        continue
    print(city)

# Looping Through a List with enumerate()
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}")

# Using else with for Loops
for city in cities:
    print(city)
else:
    print("No more cities!")

# Real-Life Example: Distributing Laddus
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")


