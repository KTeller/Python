'''
Created on Nov 21, 2021

@author: ITAUser
'''
def volumeCalculator (height, width, depth):
    area = height * width
    volume = depth * area 
    sentence = "The volume of this object is: "
    print(sentence + str(volume))
    return volume

volumeCalculator (5, 5, 5)

def shippingAndTax (subTotal):
    shipping = 10
    tax = 0.10
    taxTotal = subTotal * tax 
    total = subTotal + taxTotal + shipping 
    sentence = "The total is: "
    print(sentence + str(total))
    return total

shippingAndTax (15)
    
def circleArea (radius):
    pi = 3.14
    squared = radius * radius
    area = pi * squared
    sentence = "The area is: "
    print(sentence + str(area))
    return area
    
circleArea (5)