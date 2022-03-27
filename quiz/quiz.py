'''
Created on Mar 11, 2022

@author: ITAUser
The Objective of this program is to quiz the 
user on basic high school trivia.
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.

#Ask the user question one. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."

#Ask the user question two. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."

#Ask the user question three. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."

#Ask the user question four. And store the users answer.

#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."

#Calculate the percentage the user got. And store it in a variable called p

#Print out the users score: "You got a [score]/4. Or a [p]%."

score = 0
ansOne = input("Enter a letter: A) Mitochondria B) Nucleus C) Ribosome")
a = ("Mitochondria")
b = ("Nucleus")
c = ("Ribosome")
if(ansOne.lower() == "a"):
    score = (score + 1)
    print("Correct") 
else:
    print("Incorrect, the answer is the A")
    
y = input("Enter a letter: A) 13 B) 45 C) 50")
a = ("13")
b = ("45")
c = ("50")
if(y.lower() == "c"):
    score = (score + 1)
    print("Correct")
else:
    print("Incorrect, the answer is C")

x = input("Enter a letter: A) Slope B) Output C) I don't understand math")
a = ("Slope")
b = ("Output")
c = ("I don't understand math")
if(x.lower() == "a"):
    score = (score + 1)
    print("Correct")
else:
    print("Incorrect, the answer is A")

w = input("Enter a letter: A) Verb B) Adjective C) Noun")
a = ("Verb")
b = ("Adjective")
c = ("Noun")
if(w.lower() == "c"):
    score = (score + 1)
    print ("Correct")
else:
    print("Incorrect, the answer is C")

p = (score / 4)
print("You got [score]/4 or a [p]%.")







