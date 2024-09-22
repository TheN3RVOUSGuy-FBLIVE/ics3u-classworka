store = "No Frills"
item = "Apples"
price = 0.8
quantity = 5
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

# f string
print(f"At {store} I bought some {item}.")
# concatenation
print("They sold for $" + str(price) + " each.")
# dot format
print("I wanted to purchase {} of them.".format(quantity))
print(f"The subtotal was ${subtotal} and tax was ${round(tax, 2)}")
# f string
print(f"The total price, with tax included, was ${round(total, 2)}.")

#Q1 "f" is missing after the first opening bracket