PIN = 12345

print("WELCOME TO THE BANK OF GALLO.")
entry = int(input("ENTER YOUR PIN: "))

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

#1 while loop and if checks for something
#2 while loop can repeat if the thing it checks for is true
#3 you would need to cast entry to an integer
#4 entry would not be defined