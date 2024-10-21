message = input("What is your message? ")
vowels = ["a", "e", "i", "o", "u"]

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")
    
print(list(range(len(message))))

a_count = 0
# for i in range(len(message)):
#     letter = message[i].lower()
#     if letter == 'a':
#         a_count += 1
for i in range(len(message)):
    letter = message[i].lower()
    if letter in vowels:
        a_count += 1


print(f"\nYour message contains the letter 'a' {a_count} times.")
print(list(range(7)))
#1 prints 0 - 7 (exclusive) in a list
#2 0, 1, 2, 3, 4
#3 3, 2