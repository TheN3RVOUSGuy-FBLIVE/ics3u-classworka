total = 0
run = True

while run:
    print("I will add the numbers you give me. \n")
    num = int(input("Number: "))
    if num == 0:
        print(f"Total is {total}.")
        run = False
    else:
        total += num
        print(f"Total is : {total}")