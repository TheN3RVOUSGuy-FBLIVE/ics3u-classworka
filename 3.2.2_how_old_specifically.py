name = input("What is your name? \n")
age = int(input(f"Hi {name}, how old are you? \n"))

if age <= 16:
    print(f"You can't drive, {name}. \n")
elif 16 <= age <= 17:
    print(f"You can drive but not vote, {name}. \n")
elif 18 <= age <= 20:
    print(f"You can vote but not rent a car, {name}. \n")
else:
    print(f"You can do pretty much anything, {name}. \n")