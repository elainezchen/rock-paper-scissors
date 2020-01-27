# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# prompts user to input a RPS option
x = input("Please input either 'Rock', 'Paper', or 'Scissors': ")

if(x.lower() != "rock" and x.lower() != "paper" and x.lower() != "scissors"):
    print("That was not an accepted input. Please input a valid option next time.")
    exit()
else:
    x = x.lower()

compchoice = ["rock", "paper", "scissors"]
y = random.choice(compchoice)


