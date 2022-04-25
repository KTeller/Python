'''
Created on Apr 24, 2022

@author: Kamea
Objective: The Objective of this program is 
to make a Rock, Paper, Scissors game for the 
user to play against the computer.
'''
import random

keepPlaying = True
while (keepPlaying):
    print("Welcome to Rock Paper Scissors")
    print("Best two out of three. Press 'q' to quit")
    userScore = 0
    cpuScore = 0
    while userScore < 2 and cpuScore < 2:
        userChoice = input("rock", "paper", "scissors", "q").lower()
        choices = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(choices)
        #Compares CPU and user choice and gives scores
        if ((cpuChoice == "rock" and userChoice == "rock") or (cpuChoice == 
            "paper" and userChoice == "paper") or (cpuChoice == "scissors" and 
            userChoice == "scissors")):
            print("Draw")
            print ("User: " + str(userScore) + "CPU: " + str(cpuScore))
        elif ((cpuChoice == "rock" and userChoice == "scissors") or(cpuChoice == 
            "paper" and userChoice == "rock") or (cpuChoice == "scissors" and 
            userChoice == "paper")):
            cpuScore = cpuScore + 1
            print("You lost, try again") 
            print ("User: " + str(userScore) + "CPU: " + str(cpuScore))
        elif ((cpuChoice == "scissors" and userChoice == "rock") or (cpuChoice 
            == "rock" and userChoice == "paper") or (cpuChoice == "paper" and 
            userChoice == "scissors")):
            userScore = userScore + 1
            print("You won!")
            print ("User: " + str(userScore) + ", CPU: " + str(cpuScore))
        elif (userChoice == "q"):
            keepPlaying = False
            break
        else:
            print("Not an option, try again")
    print("Thank you for playing!")
    #Determines the winner
    if (userScore == 2):
        print("User won!")
    elif (cpuScore == 2):
        print("CPU won")
    print ("User: " + str(userScore) + ", CPU: " + str(cpuScore))
    
    

        
        
        
        
        
        