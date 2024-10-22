mes1 = input("word 1: ")
mes2 = input("word 2: ")

if mes1.lower() in mes2.lower():
    print("True")
elif mes2.lower() in mes1.lower():
    print("true")
else:
    print("false")