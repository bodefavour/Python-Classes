height = float(input("Enter your height in m: "))
weight = float(input("Enter your height in kg: "))

BMI = weight /height **2

if BMI < 18.5:
    print(f"Your BMI is {BMI}, your are underweignt")
elif BMI < 25:
    print(f"Your BMI is {BMI}, your are normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, your are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, your are obese")
else:
    print(f"Your BMI is {BMI}, your are clinically obese")