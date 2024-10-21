print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 22, 2):
    print(f"{n}. {message}")

#1 nothing happens. it is short.
#2 starts at 0 (inclusive) ends at 5 (exclusive)
#3 it is used to step
#4 starts at 0 ends at 6
#5 starts at 3 (inclusive) ends at 9 (exclusive)