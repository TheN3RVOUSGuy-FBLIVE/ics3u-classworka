print("Enter three integers: ")

num1 = int(input("Num 1: "))
while True:
    num2 = int(input("Num 2: "))
    if num2 < num1:
        print(f"{num2} is smaller than {num1}. Try again. ")
        continue
    elif num2 > num1:
        break

while True:
    num3 = int(input("Num 3: "))
    if num3 < num2:
        print(f"{num3} is smaller than {num2}. Try again. ")
        continue
    elif num3 > num2:
        break

if (num1 == num2) or (num2 == num3):
    print("Not a right triangle. ")
    exit()

elif num1 ** 2 + num2 ** 2 == num3 **2:
    print("Right triangle. ")
    exit()

else:
    print("not right triangle")
    exit()