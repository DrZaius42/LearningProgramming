#! /usr/bin/env python3
# booksOrganizer.py - Organizes Springer free books by category
import os,sys 
from pathlib import Path
from fuzzywuzzy import fuzz

os.chdir(Path.home() / 'Downloads/books/Textbooks')
books = {}
bookTitles = open(Path.home() / 'Documents/booksTitles.txt', 'r')
bookCategories = open(Path.home() / 'Documents/booksCategories.txt', 'r')
categories = []
listBooks = []
for line in bookTitles:
    line = ''.join((line.replace('\n', '')).split(' '))
    listBooks.append(line)

for line in bookCategories:
    line = ''.join((line.replace('\n', '').split(' ')))
    categories.append(line)

for i in categories:
    books[i] = []

for i, name in enumerate(listBooks):
    (books[categories[i]]).append(name)

#books is a dictionary of the form category:[books on that category]
for category in books.keys():
    if os.path.isdir(Path.cwd() / category):
        for bookByCategory in books[category]:
            for pdf in os.listdir(Path.cwd()):
                if os.path.isdir(Path.cwd() / pdf):
                    continue
                if fuzz.ratio(bookByCategory, pdf) > 60:
                    os.chdir(Path.home() / 'Downloads/books/Textbooks')
                    os.rename(Path.cwd() / pdf, Path.cwd() / category / pdf)
                else:
                    print(bookByCategory + '----' + pdf) 
    else:
        os.mkdir(Path.cwd() / category)                    
        for bookByCategory in books[category]:
            for pdf in os.listdir(Path.cwd()):
                if fuzz.ratio(bookByCategory, pdf) > 60:
                    if os.path.isdir(Path.cwd() / pdf):
                        continue
                    os.chdir(Path.home() / 'Downloads/books/Textbooks')
                    os.rename(Path.cwd() / pdf, Path.cwd() / category / pdf)
                else:
                    print(bookByCategory + '----' + pdf)