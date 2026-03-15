# Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension
# Looping Through Lists
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)

# Example: Doubling each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)

# Example: Printing Kannada food items
foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")

#  Looping Through Dictionaries
# Example: Iterating over dictionary keys
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student)

# Example: Iterating over dictionary values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)

# Example: Iterating over both keys and values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")

# for Loops with range()
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)

# List Comprehension
# Example 1: Squaring numbers in a list
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

# Example 2: Filtering even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Example 3: Uppercasing Kannada city names
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
uppercased_cities = [city.upper() for city in cities]
print(uppercased_cities)

#  Dictionary Comprehension
# Example 1: Creating a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num ** 2 for num in numbers}
print(squares_dict)

# Example 2: Converting a list of names to a dictionary of name lengths
names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

# Example 3: Filtering cities with population above 10 lakhs (Localized Example)
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)

# Splitting Strings to Create Lists
# Example 1: Splitting a sentence into words
sentence = "I love coding in Python"
words = sentence.split()
print(words)

# Example 2: Splitting a string with commas
data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)

# Example 3: Limiting the number of splits
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)

