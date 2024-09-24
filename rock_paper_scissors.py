import random

options = ("rock","paper","scisssors")
running = True

while running:

    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a choice (rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scisssors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scisssors" and computer == "paper":
        print("you win!")
    else:
        print("You lose!")

    if not  input("Play again? (y/n): ").lower()== "y":
        running = False

print("Thanks for playing!")



