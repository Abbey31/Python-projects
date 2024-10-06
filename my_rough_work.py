# # ROCK_PAPER_SCISSORS1
# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3


# print("")
# playerchoice = input("Enter...\n1 for Rock:\n2 for Scissors:\n3 for Scissors:\n ")

# player = int(playerchoice)

# if player < 1 or player > 3:
#     sys.exit("You ust enter 1 2 or 3.")

# computerchoice = random.choice("123")

# computer = int(computerchoice)

# print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
# print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")
# print("")

# if player == 1 and computer == 3:
#     print('You Win!')
# elif player == 2 and computer == 3:
#     print("You Win!")
# elif player == 3 and computer == 2:
#     print("You Win!")
# elif computer == player:
#     print("Tie Game!")
# else:
#     print("Python Wins!")
    
# LESSON ON LISTS
users = ['Dave','John','Sara']
data = ['Dave',42,True] 

emptylist = []

print("Dave" in users)

