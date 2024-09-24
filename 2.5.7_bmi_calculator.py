weight_lbs = float(input("Weight in pounds: "))

height_feet = int(input("Height in feet: "))
height_inches = int(input("Additional height in inches: "))

weight_kg = weight_lbs * 0.453592
total_height_inches = (height_feet * 12) + height_inches

height_m = total_height_inches * 0.0254

bmi = round(weight_kg / (height_m ** 2), 2)

print(f"The BMI is {bmi}")