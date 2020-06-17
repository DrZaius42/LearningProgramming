#this program is a for learning to move, delete, copy files in python
import shutil, os
from pathlib import Path
os.chdir(Path.cwd().parent)
p =  Path.cwd()
open('spam.txt', 'w').close()
shutil.copy(p / 'spam.txt', p / 'some_folder')
open('eggs.txt', 'w').close()
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')