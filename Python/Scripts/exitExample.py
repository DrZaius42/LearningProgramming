#this an example of how to terminate a program before ending itself by reaching the end of the instructions
import sys
while True:
    print('Type exit to exit the program.')
    response = input()
    if response == 'exit':
        sys.exit()
    else:
        print('You typed ' + response + '.')