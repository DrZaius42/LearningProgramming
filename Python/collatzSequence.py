#this is a program to form the collatz sequence, for an positive integer "n" if is even do n/2
#if n is odd do 3n+1 and procede
import sys

def collatz(number):
    if number % 2 == 0:
        return(number//2)
    else:
        return(3*number + 1)

print('Welcome to the Collatz Sequence generator')
while True:
    steps = 0
    print('Please enter a number: ')
    try:
        n = int(input())
        if n == 0:
            print('Invalid number!! Try another')
            continue

        while n != 1:
            n = collatz(n)
            print(n)
            steps += 1

        print('Your number took: ', steps, 'steps.')
        print('Do you want to try again?: yes/no')
        tryAgain = input()
        if tryAgain.casefold() == 'yes':
            continue
        else:
            sys.exit()
    
    except ValueError:
        print('ERROR!! You must enter a valid number.')
        

