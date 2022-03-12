'''
Created on Mar 11, 2022

@author: ITAUser
'''

def fixMyCar(problem):
    if(problem == "tire"):
        print("Replace tires.")
    elif(problem == "headlights"):
        print("Fill headlight fluid.")
    elif (problem == "door"):
        print("replace door")
    elif(problem == "gas"):
        print("Fill gas tank")
    elif(problem == "window"):
        print("Replace window")
    elif (problem == "wipers"):
        print("Replace windshield wipers")
    elif(problem == "battery"):
        print("Replace battery")
    elif (problem == "exhaust"):
        print("Replace exhaust system")
    elif(problem == "transmission"):
        print("Throw out car")
    else:
        print("Your car is fine.")
    
    return 

fixMyCar("tire")
fixMyCar("headlight")
fixMyCar("door")
fixMyCar("gas")
fixMyCar("window")
fixMyCar("wipers")
fixMyCar("battery")
fixMyCar("exhaust")
fixMyCar("transmission")
fixMyCar("Nothing")