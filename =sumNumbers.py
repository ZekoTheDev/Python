#Function not finished as user cannot quit program when it types 'quit'
def sum():
    a = 0 
    while True:
        b = eval(input('Next int: '))
        if b == 'quit':
            break
        else:
            a += b
            print(f"You added {b}, the total is now {a}")
print(sum())