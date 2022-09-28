def acronym (phrase):
    userPhrase = phrase.split()
    print(userPhrase)
    for word in userPhrase:
        print(word[0][0] , end=' ')

acronym("Central Processing Unit")
