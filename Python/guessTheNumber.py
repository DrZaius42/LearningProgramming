# this is a guessing the number game
import sys
import random
print('Welcome to guess the number\nI\'ll think of a number between 1 and 20 and you have to guess.')
num = random.randint(1, 20)
print('Tell me your guess:')
guess = int(input())
turns = 1
if guess == num:
    print('Wow!! You got it on the first try.\nWell done!!\nGoodbye <3')
    sys.exit()
while guess != num:
    if guess > num:
        print('Your guess is too big, try again.')
        print('Tell me your guess:')
        guess = int(input())
    elif guess < num:
        print('Your guess is too low, try again.')
        print('Tell me your guess:')
        guess = int(input())
    turns += 1
print('You got it!! The number was: ', num)
print('You did it in ', turns, 'turns.\nGoodbye <3')
sys.exit()