import random

list = []
list2 = []

for i in range(10):
    list.append(random.randint(1, 100))
    list2.append(list[i])

print(list2)

list[-1] = -7

print(list)