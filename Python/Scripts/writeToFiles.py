#this script is for testing file and path related functions
from pathlib import Path
import os, shelve, pprint

print(str(Path('spam', 'bacon', 'eggs')))#the functions Path creates a
#"path object" that's why it needs a str()

#the '/' lets you concatenate path objects
a = Path('spam') / 'bacon' / 'eggs'
b = 'spam' / Path('bacon/eggs')
print(str(a),'\n',str(b))


print('current directory: ',str(Path.cwd()))#to get the current working directory
os.chdir('/home/drzaius/Documents')#to change current directory
print(str(Path.cwd()))


print(str(Path.home()))#to get home dir
#os.makedirs(Path.cwd() / ('spam/eggs/chicken'))#to create a dir 
#Path(r'/home/drzaius/Documents/something').mkdir()#creating a dir with a path obj

print(Path(r'/home/drzaius/Documents/something').is_absolute())
print(Path(r'something').is_absolute())

print(os.path.abspath('something'))#returns a string of the absolute path of the argument

#to retrieve parts of a path
p = Path('/home/drzaius/Documents/test.txt')
print(p.anchor)#prints root dir, in this case '/'
print(str(p.parent))#prints the path upto the file 
print(p.name)#prints test.txt
print(p.stem)#prints test
print(p.suffix)#prints .txt
print(p.drive)#no drive in linux, print 'blank', in windows would print 'C:'

print(os.path.basename('/home/drzaius/Documents/test.txt'))#works with strings
print(os.path.basename(p))#works for path
print(os.path.dirname(p))

#to get the size of a file
print(os.path.getsize('/home/drzaius/Documents/test.txt'))
print(os.path.getsize('/home/'))#it does work for directories
totalSize = 0
for filename in os.listdir('/home/'):
    totalSize += os.path.getsize(os.path.join('/home/', filename))
print(totalSize)
print(os.listdir('/home/'))

#to list the files in a directory
print(os.listdir(Path.home()/'Documents'))

#glob()
p = Path('/home/drzaius/Documents')
files = list(p.glob('*'))#creates a list of path objects
#it is equivalent to os.listdir()
#the '*' matches multiple of any character
#the '?' matches one of any character, will not match two characters
for i in files:
    print(i, '\n')

#verify existing files and directories
print('path exists?', p.exists())
print('is a file?', p.is_file())
print('is a dir?', p.is_dir())

#use method open() to open a file
os.chdir(Path.cwd() / 'LearningProgramming')
spamFile = open(Path.cwd() / 'spam.txt')#returns a file object
print(spamFile)#printing the file object
print(spamFile.read())
sonnetFile = open(Path.cwd() / 'sonnet29.txt')
for line in sonnetFile.readlines():#after some testing, it seems the method .readlines() closes the file
    #making it unable to print the lines again without openning the file a second time
    print(line)

#to write in a file you can use:
#.write() to start from a blank file, or overwrite a file
#.append() to add to the end of a file
#baconFile = open('bacon.txt', 'w')
#baconFile.write('Hello, world!\n')
#baconFile.close()
#baconFile = open('bacon.txt', 'a')
#baconFile.write('Bacon is not a vegetable.')
#baconFile.close()
#baconFile = open('bacon.txt')
#content = baconFile.read()
#print(content)


#what happens if I use '*' to open every .txt file
anyFile = open('*.txt', 'a')
anyFile.write('\nSomething something\n')
anyFile.close()
#sadly it creates a file called '*.txt'

#to store data in binary files you can use shelve module
#the idea is that it can save variable, list, etc.
#it is treated like a dictionary
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats#adding to the 'dictionary' shelfFile the entry cats, being this a list
shelfFile.close()
#one thing to note, the objects that shelve returns when using .keys() or 
#.values(), like you would with a dictionary, are 'list like objects'
#it is recommended to past the returns to list()

#another way to save variables for future use is using pprint.pformat()
#this function returns a string of the argument you pass it
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
catsDict = pprint.pformat(cats)
#basically formats the, in this case list of dictionaries, to a string.
#this way you can save the newly created string to a variable in the same python file
#or write it to a plain text file to create your own modules

