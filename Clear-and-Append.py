# This Program clears whatever is in the list and replaces it with the letters: "d", "e", "f".

list = ['a', 'b', 'c']

def change (listOfLetters):
    listOfLetters.clear()
    listOfLetters.append("d")
    listOfLetters.append("e")
    listOfLetters.append("f")
    return listOfLetters

print(list)
change(list)
print(list)