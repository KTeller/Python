'''
Created on Mar 28, 2022

@author: ITAUser
'''

#while loops
a = 4
while (a > 1):
    print(a)
    
    a = a - 1

b = 14
while (b < 20):
    print(b)
    
    b = b + 1
    
c = 55
while (c > 50):
    print(c)
    
    c = c - 1
    
    if(c == 50):
        break 
    
#for loops
sports = ["Soccer", "Football", "Tennis"]
for x in sports:
    print(x) 
    
song = ["D", "E", "L", "I", "L", "A", "H"]
for x in song:
    print(x) 
    
movies = ["The Sorcerer's Apprentice", "Avatar", "IT", "Alice in Wonderland", "Transformers"]
for x in movies:
    print(x) 
    
    if(x == "Avatar"):
        break 
