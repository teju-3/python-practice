fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

print(fruits[1:3])  # Output: ('banana', 'cherry')

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

print("apple" in fruits)  # Output: True

my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # Output: 3

my_tuple = ("apple", "banana", "cherry")
print(my_tuple.index("banana"))  # Output: 1

genders=("male","female","other")
print(genders)

genders=("male","female","other")
print(genders)

#genders[0]="boy" causes error

print(genders [1:3])

print(genders.index("male"))

#--------------------------------------------------
s={20,2,123} #set is unordered
print(s)

#print(s[0]) #causes error

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # Output: {3}
print(intersection_set)
difference_set = set1 - set2  # Output: {1, 2}
print(difference_set)
sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
print(sym_diff_set)

fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}

fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'orange','cherry'}

fruits_set.discard("banana")  # No error if "banana" is not in the set

fruits_set.pop() #Removes a random element from the set.

fruits_set.clear()


#HOMEWORK
'''Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.'''

tuple1=(1, 2, 3, 4, 5)
print(tuple1)
#tuple[0]=10 #causes error
print(tuple1[1:3]) #Output: (2, 3)
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3) #Output: (1, 2, 3, 4, 5, 6)

'''Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?'''

my_fruits = {"apple", "banana", "cherry"}
freind_fruits = {"banana", "kiwi", "grape"}
union_fruits=my_fruits | freind_fruits
intersection_fruits= my_fruits & freind_fruits
difference_fruits=my_fruits-freind_fruits
print(union_fruits) #Output: {'apple', 'banana', 'cherry', 'kiwi', 'grape'}
print(intersection_fruits) #Output: {'banana'}
print(difference_fruits) #Output: {'apple', 'cherry'}
my_fruits.add("orange")
print(my_fruits) #Output: {'apple', 'banana', 'cherry', 'orange'}
my_fruits.remove("banana")
print(my_fruits)
my_fruits.discard("banana") #No error if "banana" is not in the set

'''Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?'''

my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
my_set = set(my_list)
print(my_tuple)
print(my_set)
#my_tuple.append(6)  # This would cause an error
my_set.add(6)  # This works
print(my_set)