name = input("What is your name?: ")

while True:
    age = input("\nHow old are you?: ")
    try:
        int(age)
        break
    except:
        print("\nThe age entered wasn't a whole number, try again.")

colour = input("\nWhat is your favourite colour?: ")

tv_show = input("\nWhat is your favourite TV show?")

print("My name is", name + ", I am", age, "years old, my favourite colour is", colour.lower(), "and my favourite TV show is", tv_show +".")
