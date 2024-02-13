# program of calculating BMI{Body Mass Index}

weight = float(input("Enter your weight"))
height = float(input("Enter your height"))
bmi = weight / (height ** 2)
print(f"Your bmi is {bmi}")
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"You are {category}")


