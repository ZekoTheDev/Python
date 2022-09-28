def calculateBMI ():
    weight = int(input("How much do you weigh: "))
    length = float(input("How tall are you: (in meters) "))
    print("BMI rapport")
    print("-----------")
    BMI = weight / (length * length)
    print(f"Your bmi is: {float(BMI)}")
    if BMI >= 30:
        print("Critically Overweight (obesitas)")
    elif BMI < 30 and BMI >= 25:
        print("Overweight")
    elif BMI < 25 and BMI >= 18.5:
        print("Healty Weight")
    else:
        print("Underweight")

calculateBMI()