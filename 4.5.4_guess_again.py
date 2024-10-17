import random

my_num = random.randrange(1, 11)
choice = int(input("I am thinking of a number from 1-10. Pick a number. \n"))

while True:
    if my_num == choice:
        print(f"Congratulations. I was thinking of {my_num}\n")
        break
    else:
        choice = int(input("Incorrect. Guess again. \n"))