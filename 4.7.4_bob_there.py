mes = input()

i = 0
found = False

while i < len(mes) - 2: 
    if mes[i].lower() == "b" and mes[i+2].lower() == "b":
        found = True
        break
    i += 1

if found:
    print("True")
else:
    print("False")