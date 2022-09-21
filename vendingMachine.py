# List (for in)
# //
# If Statement

# Variables
# Maak drie variables aan. Een die de prijs van het gekozen product vasthoud, een die het betaalde bedrag vasthoud en de derde die het verschil tussen die twee variables vasthoud.
# Maak zes variables aan die de Integers van de munteenheid kunnen vasthouden.
# Maak zes variables aan die per munteenheid laat zien, hoeveel je er bezit.
# Maak zes variables aan die het overgebleven bedrag behouden zodat je er mee kan doorrekenen.
# Stappenplan
# Zodra de gebruiker het "gekozen" product heeft ingevoerd en het "betaalde bedrag" heeft ingevoerd slaan we die data op in de variables,
# vervolgens stoppen we het verschil van die twee variables in een nieuwe variable genaamd "verschil".
# Daarna berekenen we per munt eenheid hoeveel het overgebleven bedrag is als de munteenheid doormiddel van een % eraf is gehaald.
# Dat overgebleven bedrag stoppen we een variable zodat we weer hetzelfde kunnen berekenen met een andere munteenheid.
# Zodra dit voor alle munteenheden is gedaan. Maak dan voor elke eenheid een print statement die laat zien hoeveel aantallen je van elke munt bezit.


gekozenProduct = int(input("De prijs van het gekozen product: "))
betaaldeBedrag= int(input("Het betaalde bedrag: "))
verschil = betaaldeBedrag - gekozenProduct

vijftigCent = 50
twintigCent = 20
tienCent = 10
vijfCent = 5
tweeCent = 2
eenCent = 1


aantalVijftigCent = int((verschil - (verschil % vijftigCent)) / vijftigCent)
overgebleven = verschil % vijftigCent
print(f"aantal munten van {vijftigCent} eurocent is {aantalVijftigCent}")

aantalTwintigcent = int((overgebleven - (overgebleven % twintigCent))/twintigCent)
overgebleven1 = overgebleven % twintigCent
print(f"aantal munten van {twintigCent} eurocent is {aantalTwintigcent}")

aantalTiencent = int((overgebleven1 - (overgebleven1 % tienCent))/tienCent)
overgebleven2 = overgebleven1 % tienCent
print(f"aantal munten van {tienCent} eurocent is {aantalTiencent}")

aantalvijfCent = int((overgebleven2 - (overgebleven2 % vijfCent))/vijfCent)
overgebleven3 = overgebleven2 % vijfCent
print(f"aantal munten van {vijfCent} eurocent is {aantalvijfCent}")

aantaltweeCent = int((overgebleven3 - (overgebleven3 % tweeCent))/tweeCent)
overgebleven4 = overgebleven3 % tweeCent
print(f"aantal munten van {tweeCent} eurocent is {aantaltweeCent}")

aantaleenCent = int((overgebleven4 - (overgebleven4 % eenCent))/eenCent)
overgebleven5 = overgebleven4 % eenCent
print(f"aantal munten van {eenCent} eurocent is {aantaleenCent}")






