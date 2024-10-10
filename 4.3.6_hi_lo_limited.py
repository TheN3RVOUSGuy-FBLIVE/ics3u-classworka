import random

num = random.randint(1, 100)
tries = 1
right = False

while tries < 7 and not right:
    guess = int(input("Guess a number \n"))
    if guess > num:
        print("Too high \n")
        tries += 1
    elif guess < num:
        print("Too low \n")
        tries += 1
    elif guess == num:
        print("Correct! \n")
        right = True
if tries == 7:
    print(f"You ran out of tries. I was thinking of {num}. \n")
    exit()