def calculateBMI ():
    gewicht = int(input("Geef je gewicht: "))
    lengte = float(input("Geef je lengte: (in meters) "))
    print("BMI rapport")
    print("-----------")
    BMI = gewicht / (lengte * lengte)
    print(f"Jouw bmi is: {float(BMI)}")
    if BMI >= 30:
        print("Ernstig overgewicht (obesitas)")
    elif BMI < 30 and BMI >= 25:
        print("Overgewicht")
    elif BMI < 25 and BMI >= 18.5:
        print("Gezond gewicht")
    elif BMI < 18.5:
        print("Ondergewicht")

calculateBMI()