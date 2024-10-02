earth_w = float(input("What is your earth weight? \n"))

print(f"""I have information for the following planets:
{'1. Venus':<10} {'2. Mars':<10} {'3. Jupiter':<10}
{'4. Saturn':<10} {'5. Uranus':<10} {'6. Neptune':<10}""")

planet = int(input("Enter a planet you would like to visit. \n"))

if planet == 1:
    earth_w = earth_w * 0.78
elif planet == 2:
    earth_w = earth_w * 0.39
elif planet == 3:
    earth_w = earth_w * 2.65
elif planet == 4:
    earth_w = earth_w * 1.17
elif planet == 5:
    earth_w = earth_w * 1.05
elif planet == 6:
    earth_w = earth_w * 1.23
else:
    print("Please enter a valid planet. \n")
    exit()

print(f"Your weight would be {earth_w} on that planet. \n")