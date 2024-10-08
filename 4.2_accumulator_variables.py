n = 0
total = 0

while n <= 10:
    n += 1
    total += n

print(total)

m = 100
total2 = 0
while m <= 200:
    m += 1
    total2 += m

print(total2)

o = 200
total3 = 0
while o <= 300:
    o += 1
    total3 += o

print(total3 - total2)

p = 1000
total4 = 0
while p <= 10000:
    p += 5
    total4 += p

print(total4)

q = 0
total5 = 0
while q <= 100:
    if q / 3 == q % 3:
        q += 0
    else:
        q += 5
    total5 += q

print(total5)