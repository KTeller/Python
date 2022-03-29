'''
Created on Mar 28, 2022

@author: ITAUser
'''
def counting():
    x = 0
    while (x <= 100):
        print(x)
        
        x = x + 1
        print("DONE")
        return 

counting()

def fruits(fruit):
    for x in fruit:
        print(x)
        print("DONE")
        return 

listOFruit = ["apple", "pear", "peach", "watermelon", "tomato"]
fruits(listOFruit)

def checkStudents(studentList):
    x = 0
    while (x = len(studentList[0])):
        if(studentList[0][x] == True):
            print(studentList[0][x] + " is passing.")
        else:
            print(studentList[0][x] + " is failing.")
        
    print("DONE")
    return 

listOfStudents = [["Michael", "Patrice", "Amaya", "William"], [True, True, True, False]]
checkStudents(listOfStudents)


def printGrades(studentList):
    for grade in studentList:
        print(grade)
        print("DONE")
        return 

listOfStudents = [66, 24, 12, 45, 100, 100, 100]
printGrades(listOfStudents)
