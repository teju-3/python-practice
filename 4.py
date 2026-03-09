x=5
print(x)
x+=3
print(x)
x-=2
print(x)
x*=4
print(x)
x/=6
print(x)
x%=2
print(x)

a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

y,z,w=20,40,60
print(y<z and z<w)
print(y>z or z<w) 
print(not(y<z))

text="I am a girl"
list=[1,2,3,4,5]
print("a" in text)
print("I" not in text)
print(3 in list)
print(6 not in list)


t,e,j,u=0,10,20,0
print(t and e)
print(t and j)
print(t and u)
print(t or e)
print(t or j)
print(t or u)

#HOMEWORK

o,p=10,20
print(o&p)
print(o|p)
print(o^p)
print(o<<2)
print(p>>1)

string=input("Enter a string: ")
print(string)
print("a" in string)
print("Python" not in string)

p=int(input("Enter first number: "))
q=int(input("enter second number: "))
print(p)
print(q)

print((p and q)>10)
print((p or q)<5)
print((not(p>q)))

age=int(input("Enter your age: "))
message=["You are a minor","You are an adult"]
print(message[age>=18])