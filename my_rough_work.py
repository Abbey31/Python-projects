# # ROCK_PAPER_SCISSORS 1
# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#      ROCK = 1
#      PAPER = 2
#      SCISSORS = 3


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
# users = ['Dave','John','Sara']
# data = ['Dave',42,True] 

# emptylist = []

# print("Dave" in users)  

# TUPLES
# mytuple = tuple(('Dave',42,True))
# anothertuple = (1,4,2,8,2,2)
# print(mytuple)
# print(anothertuple)

# newlist = list(mytuple)
# newlist.append('Neil')
# newtuple = tuple(newlist)
# print(newtuple)

# #Unpacking
# (one,two,*hey) = anothertuple
# print(one)
# print(two)
# print(hey)

# print(anothertuple.count(2))
#DICTIONARIES
# band = {
#     "vocals":"Plant",
#     "guitar":"Page"
# }
# band2 = dict(vocals="Plant", guitar="Page")
# print(band)
# print(band2)
# print(type(band))
# print(len(band))

# # Access items
# print(band["vocals"])
# print(band.get("guitar"))
# #list all keys
# print(band.keys())

# #List all values
# print(band.values())

# #list of key/value pairs as tuples
# print(band.items())

# #Verify existing keys
# print("guitar" in band)
# print("triangle" in band)

# #Change values
# band["vocals"] = "Coverdale"
# band.update({"bass":"JPJ"})
# print(band)

# #Reove items
# print(band.pop("bass"))
# print(band)

# band["drums"] = "Bonham"
# print(band)

# print(band.popitem()) #tuple
# print(band)

# #Delete and clear
# band["drums"] = "Bonham"
# del band["drums"]
# print(band)

# band2.clear()
# print(band2)

# del band2

# #Copying DICTIONARIES

# band2 = band # create a reference 
# print("Bad copy!")
# print(band2)
# print(band)

# band2['drums'] = "Dave"
# print(band)

# band2 = band.copy()
# band2["drums"] = "Dave"
# print("Good copy!")
# print(band)
# print(band2)
# # Copying with the dictionary constructor function
# band3 = dict(band)
# print("Good copy!")
# print(band3)

# # NESTED DICTIONARIES
# member1 = {
#     "name":"Plant",
#     "instrument":"vocals"
# }
# member2 = {
#     "name":"Page",
#     "instrument":"guitar"
# }
# band = {
#     "member1":member1,
#     "member2":member2
# }
# print(band)
# print(band["member1"]["name"])

#SETS

# nums = {1,2,3,4}

# nums2 = {1,2,3,4}

# nums2 = set((1,2,3,4))

# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums))

#NO DUPLICATES ALLOWED
# nums = {1,2,2,3}
# print(nums)
#True is a dupe of 1,False is a dupe of zero

# nums = {1,True,2,False,3,4,0}
# print(nums) 
# Check if a value is in a set
# print(2 in nums)

# but we cannot refer to an element in the set with an index position or a key

# Add a new element to a set
# nums.add(8) 
# print(nums)

# Add eleents from one set to another
# morenums = {5,6,7}
# nums.update(morenums)
# print(nums)

 # you can use update with lists,tuples, and dictionaries too.
 #Merge two sets to create a new set
# one = {1,2,3}
# two = {5,6,7}

# mynewset = one.union(two)
# print(mynewset)

#Keep only the duplicates
# one = {1,2,3}
# two = {2,3,4}
# one.intersection_update(two)
# print(one)

# Keep everything except the duplicates
# one = {1,2,3}
# two = {2,3,4}

# one.symmetric_difference_update(two)
# print(one)

#LOOPS
# value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

#names = ["Dave","Sara","John"]


# for x in names:
#     if x == "Sara":
#         break
#     print(x) 
# for x in names:
#     if x == "Sara":
#         continue
#     print(x) 
#ranges
#for x in range(4):
 #   print(x)
# for x in range(2,4):
#     print(x)
# for x in range(0,100,4):
#     print(x)
# else:
#     print("Glad that's over")
# names = ["Dave","Sara","John"]
# actions = ["codes","eats","sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".") 
#ROCK_PAPER_SCISSORS2 edited with while loop
# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#       ROCK = 1
#       PAPER = 2
#       SCISSORS = 3

# playagain = True

# while playagain:

#     playerchoice = input("\nEnter...\n1 for Rock:\n2 for Paper:\n3 for Scissors:\n ")

#     player = int(playerchoice)

#     if player < 1 or player > 3:
#         sys.exit("You ust enter 1 2 or 3.")

#     computerchoice = random.choice("123")

#     computer = int(computerchoice)

#     print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
#     print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")
    
#     if player == 1 and computer == 3:
#         print('You Win!')
#     elif player == 2 and computer == 3:
#         print("You Win!")
#     elif player == 3 and computer == 2:
#         print("You Win!")
#     elif computer == player:
#         print("Tie Game!")
#     else:
#         print("Python Wins!")

#     playagain = input("\nPlayagain? \nY for Yes or \nQ to Quit\n ")

#     if playagain.lower() == "y":
#         continue
#     else:
#         print("\n🎉🎉🎉🎉")
#         print("Thank you for playing!\n")
#         playagain = False

# sys.exit("Bye!👋")    

#FUNCTIONS
# def hello():
#     print("Hello World!")

# hello()

# def sum(num1 = 0,num2=0):
#     return num1 + num2

# total = sum(2,3)
# print(total)
# def sum(num1=0,num2=0):
#     if (type(num1) is not int or type(num2) is not int ):
#         return 
#     return num1 + num2

# total = sum(7,3)
# print(total)
# def multiple_items(*args):
#     print(args)
#     print(type(args))

# multiple_items("Dave","John","Sara")
# def mult_named_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# mult_named_items(first="Dave",last="Gray")
#RECURSION
# def add_one(num):

#     if (num >= 9):
#         return num + 1
    
#     total = num + 1
#     print(total)

#     return add_one(total)

# mynewtotal = add_one(0)
# print(mynewtotal)

#ROCK_PAPER_SCISSORS 3 WITH FUNCTION AND RECURSION
# import sys
# import random
# from enum import Enum


# def play_rps():

#     class RPS(Enum):
#         ROCK = 1
#         PAPER = 2
#         SCISSORS = 3

       
#     playerchoice = input("\nEnter...\n1 for Rock:\n2 for Paper:\n3 for Scissors:\n ")

#     if playerchoice not in ["1","2","3"]:
#         print("You ust enter 1 2 or 3.")
#         return play_rps()

#     player = int(playerchoice)
   
#     computerchoice = random.choice("123")

#     computer = int(computerchoice)

#     print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
#     print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")
    
#     if player == 1 and computer == 3:
#         print('You Win!')
#     elif player == 2 and computer == 3:
#         print("You Win!")
#     elif player == 3 and computer == 2:
#         print("You Win!")
#     elif computer == player:
#         print("Tie Game!")
#     else:
#         print("Python Wins!")

#     print("\nPlayagain?")
#     while True:
#         playagain = input("\nY for Yes or \nQ to Quit\n ")
#         if playagain.lower() not in ["y","q"]:
#             continue
#         else:
#             break

#     if playagain.lower() == "y":
#         return play_rps()
#     else:
#         print("\n🎉🎉🎉🎉")
#         print("Thank you for playing!\n")
#         sys.exit("Bye!👋")

# play_rps()
        
# SCOPE AND NESTED FUNCTIONS 
# name = "Dave"
# count = 1



# def another():
#     color = "blue"
#     global count
#     count += 1
#     print(count)

#     def greeting(name):    
#         print(color)
#         print(name)

    
#     greeting("Dave")

# another()
# ROCK_PAPER_SCISSORS 4 WITH SCOPE AND NESTED FUNCTION
# import sys
# import random
# from enum import Enum

# game_count = 0


# def play_rps():

#     class RPS(Enum):
#          ROCK = 1
#          PAPER = 2
#          SCISSORS = 3

       
#     playerchoice = input("\nEnter...\n1 for Rock:\n2 for Paper:\n3 for Scissors:\n ")

#     if playerchoice not in ["1","2","3"]:
#          print("You ust enter 1 2 or 3.")
#          return play_rps()

#     player = int(playerchoice)
   
#     computerchoice = random.choice("123")

#     computer = int(computerchoice)

#     print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
#     print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")

#     def decide_winner(player,computer):
    
#         if player == 1 and computer == 3:
#             return 'You Win!'
#         elif player == 2 and computer == 3:
#             return "You Win!"
#         elif player == 3 and computer == 2:
#             return "You Win!"
#         elif computer == player:
#             return "Tie Game!"
#         else:
#             return "Python Wins!"
        
#     game_result = decide_winner(player,computer) 
#     print(game_result)
        
#     global game_count
#     game_count += 1

#     print("\nGame count: " + str(game_count))

#     print("\nPlayagain?")
#     while True:
#         playagain = input("\nY for Yes or \nQ to Quit\n ")
#         if playagain.lower() not in ["y","q"]:
#              continue
#         else:
#              break

#     if playagain.lower() == "y":
#          return play_rps()
#     else:
#         print("\n🎉🎉🎉🎉")
#         print("Thank you for playing!\n")
#         sys.exit("Bye!👋")

# play_rps()
# CLOSURE  
#closure is a function having access to the scope of its parent function after the parent function has returned.

# def parent_function(person):
#     coins = 3

#     def play_game():
#         nonlocal coins
#         coins-= 1

#         if coins > 1:
#             print("\n" + person + "has" + str(coins) +"coins left.")
#         elif coins == 1:
#             print("\n" + person + "has" + str(coins) + "coin left.")
#         else:
#             print("\n" + person + "is out of coins.")

#     return play_game()

# tommmy = parent_function("Tommy")
# tommmy = parent_function("Timmy")

# ROCK_PAPER_SCISSORS 5 WITH CLOSURE
# import sys
# import random
# from enum import Enum

#

# def rps():
#     game_count = 0
#     player_wins = 0
#     python_wins = 0


#     def play_rps():
#         nonlocal player_wins
#         nonlocal python_wins 

#         class RPS(Enum):
#             ROCK = 1
#             PAPER = 2
#             SCISSORS = 3

        
#         playerchoice = input("\nEnter...\n1 for Rock:\n2 for Paper:\n3 for Scissors:\n ")

#         if playerchoice not in ["1","2","3"]:
#             print("You ust enter 1 2 or 3.")
#             return play_rps()

#         player = int(playerchoice)
    
#         computerchoice = random.choice("123")

#         computer = int(computerchoice)

#         print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
#         print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".\n")

#         def decide_winner(player,computer):
#             nonlocal player_wins
#             nonlocal python_wins        
#             if player == 1 and computer == 3:
#                 player_wins += 1
#                 return 'You Win!'
#             elif player == 2 and computer == 3:
#                 player_wins += 1
#                 return "You Win!"
#             elif player == 3 and computer == 2:
#                 player_wins += 1
#                 return "You Win!"
#             elif computer == player:
#                 return "Tie Game!"
#             else:
#                 python_wins += 1
#                 return "Python Wins!"
            
#         game_result = decide_winner(player,computer) 
#         print(game_result)
            
#         nonlocal game_count 
#         game_count += 1

#         print("\nGame count: " + str(game_count))
#         print("\nPlayer wins: " + str(player_wins))
#         print("\nPython wins: " + str(python_wins))

#         print("\nPlayagain?")
#         while True:
#             playagain = input("\nY for Yes or \nQ to Quit\n ")
#             if playagain.lower() not in ["y","q"]:
#                 continue
#             else:
#                 break

#         if playagain.lower() == "y":
#             return play_rps()
#         else:
#             print("\n🎉🎉🎉🎉")
#             print("Thank you for playing!\n")
#             sys.exit("Bye!👋")

#     return play_rps

# play = rps()
# play()
#F-STRINGS
# person = "Dave"
# coins = 3
# print("\n" + person + "has" + str(coins) + "coins left.")

#message = " \n %s has %s coins left." % (person, coins)
#print(message)

#message = " \n {} has {} coins left." .format (person, coins)
#print(message)
#message = " \n {person} has {coins} coins left." .format(coins=coins, person=person)
#print(message)

#player = { 'person':'Dave','coins':3}

# message = " \n {person} has {coins} coins left." .format(**player)
# print(message)
#message = f"\n{person} has {2 * 5} coins left."
#print(message)
# message = f"\n{person.lower()} has {2 * 5} coins left."
# print(message)
# message = f"\n{player['person']} has {2 * 5} coins left."
# print(message)

#Passing foratting options into string
# num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}")# the "f" stands for fixed
# for num in range(1,11):
#     print(f"\n2.25 times {num} is {2.25 * num:.2f}")
# for num in range(1,11):
#     print(f"{num} divided by  4.52 is {num/ 4.52:.2%}")
# ROCK_PAPER_SCISSORS 6 WITH STRING FORMATTING
# import sys
# import random
# from enum import Enum

# def rps():
#     game_count = 0
#     player_wins = 0
#     python_wins = 0


#     def play_rps():
#         nonlocal player_wins
#         nonlocal python_wins 

#         class RPS(Enum):
#             ROCK = 1
#             PAPER = 2
#             SCISSORS = 3

        
#         playerchoice = input("\nEnter...\n1 for Rock:\n2 for Paper:\n3 for Scissors:\n ")

#         if playerchoice not in ["1","2","3"]:
#             print("You ust enter 1 2 or 3.")
#             return play_rps()

#         player = int(playerchoice)
    
#         computerchoice = random.choice("123")

#         computer = int(computerchoice)

#         print(f"\nYou chose {str(RPS(player)).replace('RPS.','').title()}.")
#         print(f"Python chose   {str(RPS(computer)).replace('RPS.','').title()}.\n"
#         )

#         def decide_winner(player,computer):
#             nonlocal player_wins
#             nonlocal python_wins        
#             if player == 1 and computer == 3:
#                 player_wins += 1
#                 return 'You Win!'
#             elif player == 2 and computer == 3:
#                 player_wins += 1
#                 return "You Win!"
#             elif player == 3 and computer == 2:
#                 player_wins += 1
#                 return "You Win!"
#             elif computer == player:
#                 return "Tie Game!"
#             else:
#                 python_wins += 1
#                 return "Python Wins!"
            
#         game_result = decide_winner(player,computer) 
#         print(game_result)
            
#         nonlocal game_count 
#         game_count += 1

#         print(f"\nGame count: {str(game_count)}")
#         print(f"\nPlayer wins: {str(player_wins)}")
#         print(f"\nPython wins: {str(python_wins)}")

#         print("\nPlayagain?")
#         while True:
#             playagain = input("\nY for Yes or \nQ to Quit\n ")
#             if playagain.lower() not in ["y","q"]:
#                 continue
#             else:
#                 break

#         if playagain.lower() == "y":
#             return play_rps()
#         else:
#             print("\n🎉🎉🎉🎉")
#             print("Thank you for playing!\n")
#             sys.exit("Bye!👋")

#     return play_rps

# play = rps()
# play()

#MODULES
# from math import pi
# import sys
# import random as musa # we can iport as alias
# from enum import Enum  

# print(pi)
# for item in dir(musa):
#     print(dir(musa))

 
import sys
# import random
# from enum import Enum

# def rps():
#     game_count = 0
#     player_wins = 0
#     python_wins = 0


#     def play_rps():
#         nonlocal player_wins
#         nonlocal python_wins 

#         class RPS(Enum):
#             ROCK = 1
#             PAPER = 2
#             SCISSORS = 3

# ROCK_PAPER_SCISSORS 7 WITH MODULES
# import sys
# import random
# from enum import Enum

# def rps():
#     game_count = 0
#     player_wins = 0
#     python_wins = 0


#     def play_rps():
#         nonlocal player_wins
#         nonlocal python_wins 

#         class RPS(Enum):
#             ROCK = 1
#             PAPER = 2
#             SCISSORS = 3

        
#         playerchoice = input("\nEnter...\n1 for Rock:\n2 for Paper:\n3 for Scissors:\n ")

#         if playerchoice not in ["1","2","3"]:
#             print("You ust enter 1 2 or 3.")
#             return play_rps()

#         player = int(playerchoice)
    
#         computerchoice = random.choice("123")

#         computer = int(computerchoice)

#         print(f"\nYou chose {str(RPS(player)).replace('RPS.','').title()}.")
#         print(f"Python chose   {str(RPS(computer)).replace('RPS.','').title()}.\n"
#         )

#         def decide_winner(player,computer):
#             nonlocal player_wins
#             nonlocal python_wins        
#             if player == 1 and computer == 3:
#                 player_wins += 1
#                 return 'You Win!'
#             elif player == 2 and computer == 3:
#                 player_wins += 1
#                 return "You Win!"
#             elif player == 3 and computer == 2:
#                 player_wins += 1
#                 return "You Win!"
#             elif computer == player:
#                 return "Tie Game!"
#             else:
#                 python_wins += 1
#                 return "Python Wins!"
            
#         game_result = decide_winner(player,computer) 
#         print(game_result)
            
#         nonlocal game_count 
#         game_count += 1

#         print(f"\nGame count: {str(game_count)}")
#         print(f"\nPlayer wins: {str(player_wins)}")
#         print(f"\nPython wins: {str(python_wins)}")

#         print("\nPlayagain?")
#         while True:
#             playagain = input("\nY for Yes or \nQ to Quit\n ")
#             if playagain.lower() not in ["y","q"]:
#                 continue
#             else:
#                 break

#         if playagain.lower() == "y":
#             return play_rps()
#         else:
#             print("\n🎉🎉🎉🎉")
#             print("Thank you for playing!\n")
#             sys.exit("Bye!👋")

#     return play_rps

# rock_paper_scissors = rps()
# if __name__ == "__main__":
#     rock_paper_scissors()
#COMMAND_LINE_ARGUMENTS

# def hello(name, lang):
#     greetings = {
#         "English":"Hello",
#         "Spanish":"Hola",
#         "German":"Hallo",
#     }
#     msg = f"{greetings[lang]} {name}!"
#     print(msg)
# if __name__ == 'main':
#     import argparse

#     parser = argparse.ArgumentParser(
#         description="Provides a personal greeting."
#     )

#     parser.add_argument(
#         "--n", "--name", metavar="name",
#         required=True, help="The name of the person to greet."
#     )
#     parser.add_argument(
#         "--l", "--lang", metavar="language",
#         required=True, choices=["English","Spanish","German"],
#         help = "The language of the greeting."
#     )


#     args = parser.parse_args()

#     hello(args.name,args.lang)

#     msg = f"Hello {args.name}!"
#     print(msg)
# ROCK_PAPER_SCISSORS 8 WITH COMMAND_LINE_ARGUMENTS

# import sys
# import random
# from enum import Enum

# def rps(name='PlayerOne'):
#     game_count = 0
#     player_wins = 0
#     python_wins = 0

#     def play_rps():
#         nonlocal name
#         nonlocal player_wins
#         nonlocal python_wins 

#         class RPS(Enum):
#             ROCK = 1
#             PAPER = 2
#             SCISSORS = 3

        
#         playerchoice = input(f"\n{name}, please enter...\n1 for Rock:\n2 for Paper:\n3 for Scissors:\n ")

#         if playerchoice not in ["1","2","3"]:
#             print(f"{name},please enter 1 2 or 3.")
#             return play_rps()

#         player = int(playerchoice)
    
#         computerchoice = random.choice("123")

#         computer = int(computerchoice)

#         print(f"\n{name}you chose {str(RPS(player)).replace('RPS.','').title()}.")
#         print(f"Python chose   {str(RPS(computer)).replace('RPS.','').title()}.\n"
#         )

#         def decide_winner(player,computer):
#             nonlocal player_wins
#             nonlocal python_wins        
#             if player == 1 and computer == 3:
#                 player_wins += 1
#                 return f'{name},you Win!'
#             elif player == 2 and computer == 3:
#                 player_wins += 1
#                 return f"{name},you Win!"
#             elif player == 3 and computer == 2:
#                 player_wins += 1
#                 return f"{name},you Win!"
#             elif computer == player:
#                 return "Tie Game!"
#             else:
#                 python_wins += 1
#                 return f"Python Wins!\nSorry, {name}....😞"
            
#         game_result = decide_winner(player,computer) 
#         print(game_result)
            
#         nonlocal game_count 
#         game_count += 1

#         print(f"\nGame count: {game_count}")
#         print(f"\n{name}'s wins: {player_wins}")
#         print(f"\nPython wins: {python_wins}")

#         print(f"\nPlayagain,{name}?")
#         while True:
#             playagain = input("\nY for Yes or \nQ to Quit\n ")
#             if playagain.lower() not in ["y","q"]:
#                 continue
#             else:
#                 break

#         if playagain.lower() == "y":
#             return play_rps()
#         else:
#             print("\n🎉🎉🎉🎉")
#             print("Thank you for playing!\n")
#             sys.exit(f"Bye {name}!👋")

#     return play_rps


# if __name__ == "__main__":
#     import argparse

#     parser = argparse.ArgumentParser(
#         description="Provides a personalized game experience."
#     )

#     parser.add_argument(
#         "--n", "--name", metavar="name",
#         required=True, help="The name of the person  playing the game."
#     )    
#     args = parser.parse_args()

#     rock_paper_scissors = rps(args.name)
#     rock_paper_scissors()
#LAMBDA
#squared = lambda num : num * num 

#print(squared(2))


#addTwo = lambda num : num + 2

#print(addTwo(12))

#sum = lambda a, b : a + b

#print(sum(2,5))


# def funcBuilder(x):
#     return lambda num : num + x

# addTen = funcBuilder(10)
# addTwenty = funcBuilder(20)

# print(addTen(7))
# print(addTwenty(7))


# numbers = [3,7,12,18,20,21]
# squared_nums = map(lambda num: num * num,numbers) 
# print(list(squared_nums))
# numbers = [3,7,12,18,20,21]
# odd_nums = filter(lambda num : num % 2 != 0,numbers)
# print(list(odd_nums))
# from functools import reduce

# lambda acc, curr: acc + curr

# numbers = [1,2,3,4,5,1]

# total = reduce(lambda acc, curr: acc + curr,numbers)
# print(total)

# lambda acc, curr : acc + len(curr)

# names = ['Dave Gray','Sara Ito','John Jacob Jingleheimerschmidt']


# char_count = reduce(lambda acc, curr : acc + len(curr), names,0)

# print(char_count)
# CLASSES AND OBJECTS
# class Vehicle:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model


#     def moves(self):
#         print('Moves along...')

#     def get_make_model(self):
#         print(f"I'm a {self.make} {self.model}.")

# my_car = Vehicle('Mustang','Model 3')

# my_car.get_make_model()

# my_car.moves()

# your_car = Vehicle('Cadillac','Escalade')
# your_car.get_make_model()
# your_car.moves()
#INHERITANCE
# class Airplane(Vehicle):
#     def __init__(self,make,model,faa_id):
#         super().__init__(make,model)
#         self.faa_id = faa_id

#     def moves(self):
#         print('Flies along..')

# class Truck(Vehicle):
#     def moves(self):
#         print('Rumbles along..')

# class GolfCart(Vehicle):
#     pass

# cessna = Airplane('Cessna','Skyhawk','KL22')
# mack = Truck('Mack','Pinnacle')
# golfwagon = GolfCart('Yamaha','GC100')

# cessna.get_make_model()
# cessna.moves()
# mack.get_make_model()
# mack.moves()
# golfwagon.get_make_model()
# golfwagon.moves()

# print('\n\n')
#POLYMORPHISM

# for v in (my_car,your_car, cessna,mack, golfwagon):
#     v.get_make_model()
#     v.moves()

# EXCEPTIOND AND ERRORS
# class JustNotCoolError(Exception):
#     pass

# x = 2
# try:
#     raise JustNotCoolError("This ain't cool man.")
    # raise Exception("I'm a custom exception!")
    #print(x/0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
# except NameError:
#     print('Something is undefined')
# except ZeroDivisionError:
#     print('Please do not divide by zero')
# except Exception as error:
#     print(error)

# else:
#     print('No Errors')
# finally:
#     print("I'm going to print with or without an error.")
#FILE OPERATIONS
# r = Read
# a = append
# w = write
# x = Create
#f = open("names.txt")
#print(f.read())
#print(f.read(4))
#READ
#print(f.readline())

# for line in f:
#     print(line)

# f.close()

# try:
#     f = open("name_list.txt")
#     print(f.read())
# except:
#     print("The file you want to read doesn't exist")
# finally:
#     f.close() 
#APPEND
f = open("names.txt","a")
f.write("Neil")
f.close()

f = open("names.txt")
f.read()
f.close()