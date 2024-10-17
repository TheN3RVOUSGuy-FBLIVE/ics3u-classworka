import math

print("SQUARE ROOT")

while True:
    num = int(input("Enter a number: "))
    if num >= 0:
        print(f"The square root of {num} is {math.sqrt(num)}")
    
    elif num < 0:
        print("Can't take square root of negative number. ")
        continue
