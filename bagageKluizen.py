kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

keuze = int(input("Vul uw keuze in:"))

if keuze == 1 or keuze == 2 or keuze == 3 or keuze == 4:
    print(keuzes[keuze])

else:
    print("Voer een geldige cijfer in")

def aantal_kluizen_vrij():
    bestand = open('fa_testkluizen.txt', 'r+')
    kluisregels = len(bestand.readlines())
    aantalKluizen = int(12)
    aantal_kluizen_vrij = int(aantalKluizen - kluisregels)
    bestand.close()
    return aantal_kluizen_vrij

def nieuwe_kluis():
    bestand = open('fa_testkluizen.txt', 'r+').readlines()
    list = []
    for line in bestand:
        listsOfLines = line.split(";")
        list.append(listsOfLines[0])

    ints = [round(float(s)) for s in list]

    for item in ints:
        kluisnummers.remove(item)

    if len(kluisnummers) == 0:
        return -2
    else:
        kluiscode = input("Vul een kluiscode in: ")
        if len(kluiscode) < 4 or kluiscode.find(";") != -1:
            return -1
        else:
            print(f"De volgende kluizen zijn vrij: {kluisnummers}")
            kluiskeuze = input("Welke kluis zou je willen pakken?")
            bestandlezen = open('fa_testkluizen.txt', 'r+')
            bestandlezen.seek(0)
            data = bestandlezen.read(100)
            if len(data) > 0:
                bestandlezen.write("\n")
            bestandlezen.write(f"{kluiskeuze};{kluiscode}")


def kluis_openen():
    kluisnummer = input("Geef uw kluisnummer: ")
    kluiscode = input("Geef uw kluiscode: ")
    nummerEnCode = f"{kluisnummer};{kluiscode}"
    with open("fa_testkluizen.txt") as bestand:
        bestand = bestand.read().splitlines()
    bestand = open('fa_testkluizen.txt', 'r+').readlines()
    alleKluizen = ""
    for kluis in bestand:
        alleKluizen += kluis
    if alleKluizen.find(nummerEnCode) == -1:
        return False
    else:
        return True

keuzes = {
    1: "Ik wil weten hoeveel kluizen nog vrij zijn",
    2: "Ik wil een nieuwe kluis",
    3: "Ik wil even iets uit mijn kluis halen",
    4: "Ik geef mijn kluis terug"
}
print("""
    1: Ik wil weten hoeveel kluizen nog vrij zijn
    2: Ik wil een nieuwe kluis
    3: Ik wil even iets uit mijn kluis halen
    4: Ik geef mijn kluis terug
     """)