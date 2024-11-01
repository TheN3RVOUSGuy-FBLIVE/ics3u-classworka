import random

list1 = []
found = False
for i in range(10):
    a = random.randint(1, 50)
    list1.append(a)
print(list1)

e = int(input("Search for an integer: "))

for j in range(len(list1)):
    if list1[j] == e:
        found = True
        break
    else:
        found = False

if found:
    print(f"{e} found in list. ")
else:
    print(f"{e} not found. ")