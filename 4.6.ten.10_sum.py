num = int(input("pick a number: "))
total = 0

for i in range(1, num + 1):
    print(i)
    i += 1
    total += i
    
print(f"Sum: {total}")