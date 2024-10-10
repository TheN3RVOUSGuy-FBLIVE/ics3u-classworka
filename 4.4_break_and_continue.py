n = 0

while n < 10:
    n += 1
    if n == 7:
        continue
    print(n)

m = 4

#

while m < 20:
    m += 1
    if m % 3 == 0:
        continue
    print(m)

#

start = int(input("Pick a starting number: "))
end = int(input("Pick an ending number: "))
total = 0

while start < end:
    total += start
    start += 1
    if start != (13 or 31):
        continue
    if start == (13 or 31):  
        break
print(total)

#

run = True
while run:
    word = input("Pick a word: ")
    print(f"Your word is {word}. ")
    if word.lower() == "stop":
        break
print("Goodbye! \n")