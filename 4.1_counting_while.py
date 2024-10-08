print("Type in a message, and I'll display it five times.")

message = input("Message: ")
count = int(input("how many times u want to print message"))
n = 0

print()

while n < count:
    print(f"{(n + 1) * 10}. {message}")
    n += 1

#1 without n += 1, the code will run forever