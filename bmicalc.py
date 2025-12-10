print("BMI Calculator")

height  = float(input("Enter your height in meters: "))
weight  = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = " Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are under the category: {category}")