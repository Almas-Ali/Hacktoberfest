weight = int(input("Enter your weight (in kg): "))
feet = float(input("Enter your height (ft only): "))
inch = float(input("Enter your height (inch only): "))

height = feet * 0.3048 + inch * 0.0254
bmi = round(weight/(height * height), 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")