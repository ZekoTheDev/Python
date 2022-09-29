# Test Case
# 325255, Jan Jansen
# 334343, Erik Materus
# 235434, Ali Ahson
# 645345, Eva Versteeg
# 534545, Jan de Wilde
# 345355, Henk de Vries

# A Function to Format Data in a File with the help of "String Formatting" functions in Python

def textFormatter():
    with open('textfile.txt','r') as text:
        file = text.readlines()
        for index, line in enumerate(file, 1):
            cardnumber, name = line.strip('\n').split(',')
            print(f'{name} has cardnumber: {cardnumber:25}')

textFormatter()



