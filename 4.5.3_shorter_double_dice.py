import random

while True:
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    print(f"Dice rolled a {num1}!")
    print(f"Dice rolled a {num2}!")
    print(f"The total is {num1 + num2}.")
    if num1 == num2:
        print("Double Dice!")
        break