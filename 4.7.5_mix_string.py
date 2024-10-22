a = input("type soemthing ")
b = input("type someting ")
i = 0
minlength = 0

remain = ""
new = ""

if len(a) >= len(b):
    minlength = len(b)
    remain = a
else:
    minlength = len(a)
    remain = b

for i in range(minlength):
    new += a[i] + b[i]
    i += 1

new += remain[i:]

print(new)