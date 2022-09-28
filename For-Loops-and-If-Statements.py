# Program to check if person is allowed to vote

age = int(input("How old are you: "))
hasPassport = input("Do you own a Dutch Passport (yes/no)")

if hasPassport == "yes" and age >= 18:
    print("Congratulations, you can vote!")
else:
    print("Unfortunately you are not allowed to vote!")

# Program to check if person passed a test

score = int(input("What is your score: "))
if score >= 15:
    print(f"Congratulation!\nYou passed with a score of {score}!")
else:
    print("Unfortunately you did not pass the exam!")

# Program that loops trough a list of days and prints the first three letters

days = ["monday", "tuesday", "wednesday"]
for day in days:
    print(day[0:2])

# Program that loops trough a list and only prints even numbers

getallen = [1,2,3,4,5,6,7,8,9,10]

for getal in getallen:
    if getal % 2 == 0:
        print(getal)