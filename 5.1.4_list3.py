import random

list = []

for i in range(1000):
    list.append(random.randint(10, 99))
    print(list[i], end = "  ")