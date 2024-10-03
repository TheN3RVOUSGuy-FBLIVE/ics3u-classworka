print("Two questions. \nThink of an object and I'll try to guess it. \n")
q_one = input("Q1 - Is it an animal, vegetable, or mineral? \n")

if q_one.lower == "animal":
    q_two = input("Is it bigger than a breadbox? \n")
    if q_two.lower == "yes":
        print("My guess is that you are thinking of a moose. \n")
    elif q_two.lower == "no":
        print("My guess is that you are thinking of a squirrel. \n")
    else:
        print("Please answer with 'yes' or 'no'. \n")
        exit()

elif q_one.lower == "vegetable":
    q_two = input("Is it bigger than a breadbox? \n")
    if q_two.lower == "yes":
        print("My guess is that you are thinking of a watermelon. \n")
    elif q_two.lower == "no":
        print("My guess is that you are thinking of a carrot. \n")
    else:
        print("Please answer with 'yes' or 'no'. \n")
        exit()

elif q_one.lower == "mineral":
    q_two = input("Is it bigger than a breadbox? \n")
    if q_two.lower == "yes":
        print("My guess is that you are thinking of a Camaro. \n")
    elif q_two.lower == "no":
        print("My guess is that you are thinking of a paper clip. \n")
    else:
        print("Please answer with 'yes' or 'no'. \n")
        exit()

else:
    print("Please pick a valid option. \n")
    exit()