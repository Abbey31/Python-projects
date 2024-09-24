import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n") #print("")also does the same as \n for a newline

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3. ")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")
    

    if player == 1 and computerchoice == 3:
        print("You win!🎉🎉")
    elif player == 2 and computerchoice == 3:
        print("You win!🎉🎉")
    elif player == 3 and computerchoice == 2:
        print("You win!🎉🎉")
    elif player == computer:
        print("Tie game!.😩😩")

    else:
        print("Python wins!🐍🐍")

    playagain = input("\nPlayagain? \nY for Yes or \nQ to quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False # break will also work here
sys.exit("Bye!👋👋👋")
 