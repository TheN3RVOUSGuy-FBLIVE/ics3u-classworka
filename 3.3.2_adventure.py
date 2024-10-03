print("WELCOME TO VINCENT'S TINY ADVENTURE! \n")

choice = input("""You are in a creepy house! \nWould you like to go 'upstairs' or into the 'kitchen'? \n""")

if choice.lower() == "upstairs":
    choice_2 = input("""\nUpstairs you see a hallway. At the end of the hallway is the master 'bedroom'.
There is also a 'bathroom' off the hallway.
Where would you like to go? \n""")
    if choice_2.lower() == "bedroom":
        choice_3 = input("""\nYou are in a plush bedroom, with expensive-looking hardwood furniture. The bed is unmade. 
In the back of the room, the closet door is ajar. Would you like to open the door? ('yes' or 'no') \n""")
        if choice_3.lower() == "yes":
            print("\nA dark figure jumps at you and that was the last thing you ever saw. \n")
            exit()
        elif choice_3.lower() == "no":
            print("""\nWell, then I guess you'll never know what was in there.
Thanks for playing, I'm tired of making nested if statements. \n""")
            exit()
        else:
            print("\nPlease pick 'yes' or 'no'. \n")
            exit()
    elif choice_2.lower() == "bathroom":
        choice_3 = input("""\nYou are in a dirty bathroom, with an overflowing trash can and a closed toilet.
What would you like to interact with? \n""")
        if choice_3.lower() == "trash" or "trash can":
            print("\nYou find nothing but rolls of toilet and tissue paper. \n")
            exit()
        elif choice_3.lower() == "toilet" or "closed toilet":
            print("\nA creature pulls you in and you faint. \n")
            exit()
        else:
            print("\nPlease pick a valid option. \n")
    else:
        print("\nPlease pick a valid option. \n")
        exit()
elif choice.lower() == "kitchen":
    choice_2 = input("""\nThere is a long countertop with dirty dishes everywhere. Off to one side
there is, as you'd expect, a refrigerator. You may open the 'refrigerator'
or look in a 'cabinet'. \n""")
    if choice_2.lower() == "refrigerator":
        choice_3 = input("""\nInside the refrigerator you see food and stuff. It looks pretty nasty.
Would you like to eat some of the food? ('yes' or 'no') \n""")
        if choice_3.lower() == "yes":
            print("\nYou eat it and feel disgusted, but you feel like you had a months worth of food consumed. \n")
            exit()
        elif choice_3.lower() == "no":
            print("\nYou die of starvation... eventually. \n")
            exit()
        else:
            print("\nInvalid option. \n")
            exit()
    elif choice_2.lower() == "cabinet":
        choice_3 = input("""\nInside the cabinet you find a wand and a chest.
What would you like to interact with? \n""")
        if choice_3.lower() == "wand":
            print("\nYou feel power surging through your veins like you could do anything. \n")
            exit()
        elif choice_3.lower() == "chest":
            print("""\nBlack powder flies out of the chest and out the window into the air, veiling the sky.
You just released a virus into the city. \n""")
            exit()
        else:
            print("\nPlease pick a valid option. \n")
    else:
        print("\nPlease pick a valid option. \n")
else:
    print("\nPlease pick a valid option. \n")
    exit()