# With this program the first letter of Each word will be saved, capitalized and returned. Example: random access memory becomes, RAM.

def acronym (phrase):
    userPhrase = phrase.upper().split()
    print(userPhrase)
    for word in userPhrase:
        print(word[0][0] , end=' ')

acronym("central processing unit")
