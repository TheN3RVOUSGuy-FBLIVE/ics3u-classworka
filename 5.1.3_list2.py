import random

list = []

for i in range(10):
    list.append(random.randint(1, 100))
    print(f"slot {i} contains a {list[i]}")