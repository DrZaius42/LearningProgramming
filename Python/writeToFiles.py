#this script is for testing file and path related functions
from pathlib import Path
import os

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