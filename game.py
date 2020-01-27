# game.py

print("Rock, Paper, Scissors, Shoot!")

# prompts user to input a RPS option
x = input("Please input either 'Rock', 'Paper', or 'Scissors': ")

if(x.lower() != "rock" or x.lower() != "paper" or x.lower() != "scissors"):
    print("That was not an accepted input. Please input a valid option next time.")
    exit()
else:
    print(x)
