fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']

fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'cherry',' grape']

fruits.remove("orange")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry',' grape']

fruits.pop()  # Removes the last item
print(fruits)  # Output: ['apple', 'kiwi',' cherry']

fruits.pop(0)  # Removes the first item
print(fruits)  # Output: ['kiwi','cherry']

fruits.clear()
print(fruits)  # Output: []

fruits = ["apple", "banana", "cherry"]

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)

print(len(fruits))  # Output: 3

numbers = [5, 2, 9, 1]
print(sorted(numbers))  # Output: [1, 2, 5, 9]
print(numbers)  # Original list remains unchanged: [5, 2, 9, 1]

numbers = [1, 2, 3, 4]
print(sum(numbers))  # Output: 10

print(fruits.index("apple"))  # Output: 0

numbers = [1, 2, 3, 1, 1]
print(numbers.count(1))  # Output: 3

fruits.reverse()
print(fruits)  # Output: ['cherry', 'orange', 'apple']

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)

#HOMEWORK

colours=["blue","black","white"]
print(colours)
colours.append("yellow")
print(colours)
colours.insert(1,"pink")
print(colours)
colours.pop(2)
print(colours)

num=[67,34,98,12,34,26,73]
print(num)
print(sorted(num,reverse=True))
num.reverse()
print(num)