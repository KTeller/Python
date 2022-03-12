'''
Created on Mar 4, 2022

@author: ITAUser
'''

grade = 65
if grade >= 80:
    print("Passing")
elif 80 > grade >= 60:
    print("Probation")
else:
    print("Failing")
    
a = 302
if a >= 100 or a <= -100:
    print("a is a three digit number")
elif 100 > a > -100:
    print("a is not a three digit number")
    
age = 17
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
answer = "d"
if ["a", "b", "d"]:
    print("Wrong")
elif "c":
    print("Correct")
    
b = 5 < 0
c = -2 >= -1
if b and c == True:
    print("Both")
elif b or c == True:
    print("Only one")
else:
    print("Neither")
