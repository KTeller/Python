'''
Created on Jan 29, 2022

@author: ITAUser
'''
#Debug drill 1
def comparisonDrill(a, b):
    if(a < b):
        print("A is less than B.")
    elif(a == b):
        print("A is equal to B.")
    elif(a > b):
        print("A is greater than B.")
    
    return 

comparisonDrill(2, 3)
comparisonDrill(3, 3)
comparisonDrill(4, 3)

#Debug drill 2

def comparisonDrillTwo(userText, correctAnswer):
    if(userText == correctAnswer):
        print("CORRECT!")
    
    return 

comparisonDrillTwo("YES", "YES")
comparisonDrillTwo("NO", "YES")

#Debug drill 3

def shippingAndTax(subtotal):
    shipping = 0
    tax = .10
    
    if(subtotal == 15):
        shipping = 5
    if(subtotal > 15):
        shipping = 10
    if(subtotal < 15):
        shipping = 0
    
    taxTotal = subtotal * tax
    total = subtotal + taxTotal + shipping
    print("The total is: ", total)
    return total

shippingAndTax(10)
shippingAndTax(15)
shippingAndTax(20)
shippingAndTax(101)