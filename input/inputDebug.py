'''
Created on Dec 8, 2021

@author: ITAUser
'''

def circleArea():
    radius = input("What is the radius of your circle?")
    
    pi = 3.14
    squared = int(radius) * int(radius)
    area = pi * squared 
    print("The area is: " + area)
    return area


circleArea()

def rectangleArea():
    height = input("What is the height of your rectangle?")
    width = input("What is the width of your rectangle")
    
    area = int(height) * int(width)
    print(area)
    return area


rectangleArea()