print("BMI Calculator")

your_height  = float(input("Enter your height in meters: "))
your_weight  = float(input("Enter your weight in kilograms: "))

BMI= your_weight / (your_height ** 2)

if BMI < 18.5:
    category = " Underweight"
elif 18.5 <= BMI< 24.9:
    category = "Normal weight"
elif 25 <= BMI < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is: {BMI:.2f}")
print(f"You are under the category: {category}")
