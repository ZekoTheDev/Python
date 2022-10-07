# Input a dictionary that contains a key/value a pair of student/grade. This Program will return the students that scored higher than 9.0.

myStudentList = {'Bruce Lee': 9.4, 'Muhammed Ali': 9.8, 'John Doe': 8.9}

def gradeFilter(studentList):
    newDict = dict()
    for (key, value) in studentList.items():
        if value > 9.0:
            newDict[key] = value
    return newDict

print(gradeFilter(myStudentList))