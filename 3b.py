firstname="Tejaswini"
lastname="S"
fullname=firstname +" "+ lastname #concatenation
print(fullname)

w="Hello! "*9 #printing multiple times
print(w)

q="Teju is a good girl"
print(q.upper())
print(q.lower())
print(q.replace("good","smart"))

s="    Hello World!    "
print(s.strip()) #separating spaces

print(len(q)) #finding length

name="tejaswini" #slicing
print(name[:10]) 
print(name[0:])
print(name[2:5])
print(name[-3:])


u="I am \n20 years old"
print(u)

y="I am \t20 years old"
print(y)

#HOMEWORK

name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(name)
print(age)
print(f"Hello! {name},you are {age} years old." )

sen="      Python is a easy language     "
print(sen.upper())
print(sen.lower())
print(sen.replace(" ","_"))
print(sen.strip())

i="I like Blue Colour"
print(len(i.replace(" ","")))



print("Hello \n\tWorld \nThis is a backslash: \\") #we need to add extra slash bcz python considers single slash as an escape character

''' Hello
    World
This is a backslash: \ '''

text=input("Enter a text: ")
print(len(text.replace(" ","")))

h="This is Tejaswini S, studying \n 6th semester\ cse"
print(h)