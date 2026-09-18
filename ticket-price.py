name = input("What's your name?: ").strip()
while True:
    student = input("\nAre you a student (y/N): ").strip()
    if student.lower() == "n" or student.lower() == "":
        student = False
        break
    elif student.lower() == "y":
        student = True
        break
    else:
        print("Please enter y for yes, or n for no.")

while True:
    age = input("\nHow old are you?: ").strip()
    try:
        age = int(age)
        if age < 0 or age > 120:
            raise
        else:
            break
    except:
        print("The age you enter must be a whole number between 0 and 120.")

if age < 12:
    price = 5
elif age <=12 and age <= 17:
    price = 7
elif age <=18 and age <= 64:
    price = 10
else:
    price = 6

if age >= 18 and student:
    price = price - 2

print("\nYour final ticket price is £" + str(price))
