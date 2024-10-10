import random

my_num = random.randrange(1, 11)
choice = int(input("I am thinking of a number from 1-10. Pick a number. \n"))
run = True
tries = 1
while run:
    if my_num == choice:
        print(f"Congratulations. I was thinking of {my_num}\n")
        print(f"It took you {tries} tries.")
        exit()
        run = False
    else:
        choice = int(input("Incorrect. Guess again. \n"))
        tries += 1