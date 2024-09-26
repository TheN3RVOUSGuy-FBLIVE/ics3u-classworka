name = input("What is your name? \n")
age = int(input(f"Hi {name}. What is your age? \n"))

if age < 16:
    print("You cannot drive. \n")

if age < 18:
    print("You cannot vote. \n")

if age < 21:
    print("You cannot rent a car. \n")

elif age > 21:
    print("You can do anything that's legal. \n")