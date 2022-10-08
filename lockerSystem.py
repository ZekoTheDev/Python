# This Program consist of four functions and one text file in order to work.
# The text file needs to be in the same directory as this program and needs to have the following name "safeDatabase.txt"
# amountOfavailableSafes() iterates over the lines in the text file to see howmuch safes are availlable (each filled line equals a taken safe)
# menu() contains a dictionairy of menu options that will redirect the user to the function which he/she selected
# newSafe() will add a new safe to the text file if there is a safe availlable. The user needs to provide a valid safe number and pin in order to claim the safe
# opensafe() will read the file and compare the user input (combination of safe number & pin) to all the lines in the text file, to see wether the user owns a safe. If this is valid the safe will open

availableSafes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def amountOfavailableSafes():
    file = open('safeDatabase.txt', 'r+')
    safesTaken = len(file.readlines())
    totalAmountOfsafes = int(12)
    availableSafes = totalAmountOfsafes - safesTaken
    file.close()
    return f"There are {availableSafes} safes availlable!"

def menu():
    choices = {
        1: "I want to know how many safes are still available",
        2: "I want a new safe",
        3: "I want to get something out of my safe",
        4: "I am returning my safe (not available yet)"
    }
    print(f"1: {choices[1]}\n"
          f"2: {choices[2]}\n"
          f"3: {choices[3]}\n"
          f"4: {choices[4]}\n")
    choice = int(input("Select a option: "))

    if choice == 1:
        return amountOfavailableSafes()

    elif choice == 2:
        return newSafe()

    elif choice == 3:
        return opensafe()

    else:
        print("Select a valid number")

def newSafe():
    file = open('safeDatabase.txt', 'r+').readlines()
    list = []
    for line in file:
        listsOfLines = line.split(";")
        list.append(listsOfLines[0])

    ints = [round(float(s)) for s in list]

    for item in ints:
        availableSafes.remove(item)

    if len(availableSafes) == 0:
        return "All safes are taken!"
    else:
        safePin = input("Please enter your safe pin: ")
        if len(safePin) < 4 or safePin.find(";") != -1:
            return -1
        else:
            print(f"The following Safes are availlable: {availableSafes}")
            safeChoice = input("Which safe would you like to take: ")
            safeFile = open('safeDatabase.txt', 'r+')
            safeFile.seek(0)
            data = safeFile.read(100)
            if len(data) > 0:
                safeFile.write("\n")
            safeFile.write(f"{safeChoice};{safePin}")

def opensafe():
    safeNumber = input("Please enter your safenumber: ")
    safePin = input("Please enter your safe pin: ")
    numberAndPin = f"{safeNumber};{safePin}\n"
    file = open('safeDatabase.txt', 'r+').readlines()
    allsafes = ""
    for safe in file:
        allsafes += safe
    if allsafes.find(numberAndPin) == -1:
        return "Your safe number or pin is incorrect!"
    else:
        return "Your safe is now opened!"

print(menu())