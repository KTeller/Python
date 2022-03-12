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

z = int("What is the powerhouse of he cell?")
a = ("Mitochondria")
b = ("Nucleus")
c = ("Ribosome")
if z.lower() == "a":
    print("Correct") 
    score = (score + 1)
else:
    print("Incorrect, the answer is the A")
    
y = int("How many states comprise the United States?")
a = ("13")
b = ("45")
c = ("50")
if y.lower() == "c":
    print("Correct")
    score = (score + 1)
else:
    print("Incorrect, the answer is C")

x = int("In y = mx + b, what does m stand for?")
a = ("Slope")
b = ("Output")
c = ("I don't understand math")
if x.lower() == "a":
    print("Correct")
    score = (score + 1)
else:
    print("Incorrect, the answer is A")

w = int("In English, a person, place or thing is called:")
a = ("Verb")
b = ("Adjective")
c = ("Noun")
if w.lower() == "c":
    print ("Correct")
    score = (score + 1)
else:
    print("Incorrect, the answer is C")

p = (score / 4)
print("You got [score]/4 or a [p]%.")







