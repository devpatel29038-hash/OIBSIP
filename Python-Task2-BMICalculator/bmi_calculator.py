print("================================")
print("       BMI CALCULATOR")
print("================================")

try:
    # Take input from user
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Validate input
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")

    else:
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display BMI
        print("\nYour BMI is:", round(bmi, 2))

        # Classify BMI
        if bmi < 18.5:
            print("Category: Underweight")

        elif bmi < 25:
            print("Category: Normal")

        elif bmi < 30:
            print("Category: Overweight")

        else:
            print("Category: Obese")

except ValueError:
    print("Error: Please enter valid numeric values.")

print("\nThank you for using BMI Calculator!")