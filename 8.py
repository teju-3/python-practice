time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")

time = 18  # 6 PM
if time == 20:
    print("It's time for dinner!")
else:
    print("It's not dinner time yet.")

time = 15  # 3 PM

if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not a meal time.")

age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

age = 16
has_student_id = True

if age < 18 and has_student_id:
    print("You are eligible for the student discount!")
else:
    print("You are not eligible for the student discount.")

age = 65

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")

day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")

age = 19

if age >= 18:
    print("You are eligible to vote.")
    print("Remember to bring your voter ID.")
else:
    print("You are not eligible to vote.")

day = "Sunday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday.")

#HOMEWORK

age=int(input("Enter your age:"))
if(age<5):
    print("Bus Pass is free")
elif(age>=60):
    print("You get a senior citizen discount")
else:
    print("Pay the full price")

time=int(input("Enter the time: "))
if(time==8):
    print("Its time for breakfast")
elif(time==13):
    print("its time for lunch")
elif(time==20):
    print("its time for dinner")
else:
    print("its not meal time")


age=int(input("Enter your age: "))
if(age<18):
    print("You get a student membership")
elif(age>=60):
    print("You get a senior citizen membership")
else:
    print("You get a regular membership")