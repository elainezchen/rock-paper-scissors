# game.py

# imports library for random choice
import random

# welcome message
print("Rock, Paper, Scissors, Shoot!")
print("-------------------\nWelcome to my Rock-Paper-Scissors game...\n-------------------")

# prompts user to input a RPS option
x = input("Please input either 'Rock', 'Paper', or 'Scissors': ")

# tests if the input is valid and exits the program if it is not one of three options
if(x.lower() != "rock" and x.lower() != "paper" and x.lower() != "scissors"):
    print("That was not an accepted input. Please input a valid option next time.")
    exit()
else:
    x = x.lower()

# creates a list of rock paper scissors options and stores the computer's random choice in 'y'
compchoice = ["rock", "paper", "scissors"]
y = random.choice(compchoice)

# tests possible combinations for the RPS game and presents a message depending on the game
if(x == y):
    msg = "You have tied with the computer."
elif(x == "rock" and y == "paper"):
    msg = "Oh, the computer won. It's ok."
elif(x == "rock" and y== "scissors"):
    msg = "You've won! Congrats!"
elif(x == "paper" and y == "rock"):
    msg == "You've won! Congrats!"
elif(x == "paper" and y == "scissors"):
    msg = "Oh, the computer won. It's ok."
elif(x == "scissors" and y == "rock"):
    msg = "Oh, the computer won. It's ok."
else:
    msg == "You've won! Congrats!"

# final message to user
print("You chose: " + x)
print("The computer chose: " + y)
print("-------------------\n" + msg + "\n-------------------")
print("Thanks for playing. Please play again!")
