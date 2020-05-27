#this a program to test if you can write on the same python file you open 
import sys

print('Type what to add to the file')
a = input()
myFile = open('openSameFileTest.py','a')
myFile.write(a)
myFile.close()
I want to add this line to the end of this same file