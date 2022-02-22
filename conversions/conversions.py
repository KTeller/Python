'''
Created on Feb 22, 2022

program will convert miles into feet and yards
@author: Kamea Teller
'''
#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.

#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
#
#Store the value in a variable called yards and print it out with a 
#simple statement.

#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
#
#Store the value in a variable called feet and print it out with a 
#simple statement.

#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
#
#Store the value in a variable called inches and print it out with a 
#simple statement.


miles = int(input("How many miles would you like to convert?"))

yards = int(miles) * 1760
sentence = ("Converted into yards: ")
print(sentence + str(yards))


feet = int(miles) * 5280
sentence = ("Converted into feet: ")
print(sentence + str(feet))

inches = int(miles) * 63,360
sentence = ("Converted into inches: ")
print(sentence + str(inches))