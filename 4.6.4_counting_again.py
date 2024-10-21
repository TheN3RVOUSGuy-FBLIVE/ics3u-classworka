fro = int(input("Count from: "))
num = int(input("Count to: "))
skip = int(input("Count by: "))

for i in range(fro, num + 1, skip):
    print(i, end=" ")