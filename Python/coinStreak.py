#this program calculates de probability of a certain amount of streaks in a coin flip
import random

numberOfStreaks = 0
streak = 0
lastFlip = None
for flip in range(100000):
    side = random.randint(0,1)#if zero means tails and 1 means head

    if side == lastFlip:
        streak += 1
    else:
        streak = 0
    
    if streak == 6:
        streak = 0
        numberOfStreaks += 1
    
    lastFlip = side

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
