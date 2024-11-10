import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, too low guess again')
        elif guess > random_number:
            print('Sorry, too high guess again')

    print(f'Congrats you guessed the number {random_number} correctly ')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'The computer guess your number,{guess} correctly!')
computer_guess(10)


guess(10)