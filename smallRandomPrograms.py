# Oplossing 1
# resultaat = 0
# laatstegetal = 1
# while True:
#     try:
#         nummer = int(input('Voer een getal in: '))
#         laatstegetal = nummer
#         resultaat = laatstegetal * nummer
#     except ValueError:
#         print(resultaat)
#         break

# Oplossing 2
import math
lst = []
number1 = int(input('number 1: '))
number2 = int(input('number 2: '))
number3 = int(input('number 3: '))
lst.extend([number1,number2,number3])
lst.remove(max(lst))
lst.remove(min(lst))
print(f'The number in the middle is: {lst[0]}')

# Oplossing 3
# def isPositiefEnKleinerDan(x, y):
#     if x >= 0 and x < y:
#         return True
#     else:
#         return False

# Oplossing 4

# string = input('Voer een string in: ')
# omgedraaid = ''
# for letter in string:
#     omgedraaid = letter + omgedraaid
# print(f"Deze string omgekeerd: {omgedraaid}")
