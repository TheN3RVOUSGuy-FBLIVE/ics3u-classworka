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

count = 0

if found:
    for u in range(len(list1)):
        if list1[u] == e:
            count += 1
    print(f"{e} found {count} time(s) in list. Took {j + 1} attempt(s). ")
else:
    print(f"{e} not found. Searched through {j + 1} number(s). ")