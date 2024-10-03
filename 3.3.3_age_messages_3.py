name = input("What is your name? \n")
age = int(input(f"\nHello {name}, what is your age? \n"))

if age < 16:
    print("You can't drive.")
if age >= 16 and age <= 17:
    print("You can drive but not vote.")
if age >= 18 and age <= 24:
    print("You can vote but not rent a car.")
if age >= 25:
    print("You can do pretty much anything.")
