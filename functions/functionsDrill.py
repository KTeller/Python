'''
Created on Mar 30, 2022

@author: ITAUser
'''
#Function takes the difference of two numbers
def difference(numOne, numTwo):
    diff = numOne - numTwo
    print(diff)
    return diff

difference(23, 7)

#Function divides a number by 2, multiplies it by 77, then adds 10,000
def math(x):
    div = x / 2
    mult = div * 77
    add = mult + 10000
    print(add)
    return add

math(12)

#Function compares two numbers
def equal(numberOne, numberTwo):
    if(numberOne == numberTwo):
        print("True")
    else:
        print("False")
    return 

equal(98, 26)

#Function compares two numbers and returns the bigger
def bigger(maybeBig, maybeSmall):
    if(maybeBig > maybeSmall):
        print(maybeBig)
    elif(maybeSmall > maybeBig):
        print(maybeSmall)
    elif(maybeBig == maybeSmall):
        print(maybeBig)
    return

bigger(8, 5)

#Function adds two words together
def wordMath(wordOne, wordTwo):
    words = (wordOne + wordTwo)
    print (words)
    return

wordMath("Hello", "World")
    
#Function compares two numbers to the first
def comparing(oneNum, twoNum, threeNum):
    if (oneNum == twoNum) or (oneNum == threeNum):
        print("True")
    else:
        print("False")
    return 

comparing(3, 8, 3)

#Function prints my name
def name():
    print("Kamea")
    
name()

#Function compares to my favorite color
def favColor(string):
    if (string == "Blue"):
        print("Thats my favorite color!")
    else:
        print("That is not my favorite color. Try again.") 
favColor("Red")

#Function takes a number and subtracts one until it reaches zero
def loops(num):
    while (num > 0):
        print(num)
        num = num - 1
    
        if (num == 0):
            break
    return
 
loops(3)