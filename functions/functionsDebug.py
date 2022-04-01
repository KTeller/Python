'''
Created on Apr 1, 2022

@author: ITAUser
'''

'''
This function converts ounces to gallons using three steps. It takes one
integer parameter: ounces.
First, it converts ounces to cups.
Second, converts cups to quarts.
Third, converts quarts to gallons.
Finally, it returns gallons.
'''
def ouncesToGallons(ounces):
    #There are eight ounces in a cup
    cups = ounces / 8
    
    #There are four cups in a quart
    quarts = cups / 4
    
    #There are four quarts in a gallon
    gallons = quarts / 4
    
    return gallons


ouncesToGallons(24)


'''
This function converts gallons to ounces using three steps. It takes one
integer parameter: gallons.
First, it converts gallons to quarts.
Second, converts quarts to cups.
Third, converts cups to ounces.
Finally, it returns ounces.
'''
def gallonsToOunces(gallons):
    #There are four quarts in a gallon
    quarts = gallons * 4
    
    #There are four cups in a quart
    cups = quarts * 4
    
    #There are 8 ounces in a cup
    ounces = cups * 8
    
    return ounces

gallonsToOunces(24)
gallonsToOunces(4)


'''
This function converts grams to pounds using two steps. It takes one integer
parameter: grams.
First, it converts grams to ounces.
Second, it converts ounces to pounds.
Then it returns pounds.
'''
def gramsToPounds (grams):
    #There are .035 ounces in a gram
    ounces = grams * .035
    
    #There are 16 ounces in one pound
    pounds = ounces / 16
    
    return pounds

gramsToPounds(360)


'''
This function converts pounds to grams using two steps. It takes one integer
parameter: pounds.
First, it converts pounds to ounces.
Second, it converts ounces to grams.
Then it returns grams.
'''
def poundsToGrams(pounds):
    #There are 16 ounces in one pound
    ounces = pounds * 16
    
    #There are .035 ounces in a gram
    grams = ounces / .035
    
    return grams

poundsToGrams (360)

