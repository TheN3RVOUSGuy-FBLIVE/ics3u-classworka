print("Enter the following information about an item you wish to purchase..\n")

name = input("The name of the item:")

price = float(input("The price: $"))

quantity = int(input("How many do you want"))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

#1 Price is a float and name is a string. Also it asks the question with the input.
#3 A prompt is a cue for the user to enter something. Switching the order causes a problem because it asks for input before the prompt.
#4 The int() and float() functions are used to cast strings into integers or floats so they can be multiplied later on. If you remove them it will give you an error.