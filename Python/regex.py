#this a program to test regular expressions
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#the string is the regex,
#re.compile() transforms it to a regex object, must be a raw string(you have to add r at the beginning)
#\d stands for digit
mo = phoneNumRegex.search('My number is 415-555-4242.')#.search() returns a match object if the pattern is found, returns None otherwise
print('Phone number found: ' + mo.group())

#regex defines groups with parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is 415-555-1212')
mo.group(1)
print('group 1: ' + mo.group(1))
#to retrieve all groups at once mo.groups(), note the plural
print(mo.groups())

#to use special characters like parentheses you have to escape them
newRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')#here the parentheses are part
#of the first group, so to count as so must be escaped
matchObj = newRegex.search('My phone number is (415) 555-4242.')
print(matchObj.group(1))
print(matchObj.group(2))
#other special characters are: . ^ $ * + ? {} [] \ | ()

#to match several expressions use the pipe "|", as always, returns the first instance
heroRegex = re.compile(r'Batman|Spider-man')
mo1 = heroRegex.search('Batman and Spider-man')#basically works like an "or"
print(mo1.group())
mo2 = heroRegex.search('Spider-man and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|copter|mobile|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))#returns the matched text inside the parentheses in the regex "mobile"

#to match patterns optionally use the "?"
batRegex = re.compile(r'Bat(wo)?man')#regex mathches zero or one instance of the optional part
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
print(mo2.group())

#to match patterns optionally, but as many times as they appear
#use *
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())

#to match patterns the appear at least once use +
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')#should return None since "wo" is not in the string
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(str(mo1), mo2.group(), mo3.group())

#to match a certain amount of a pattern use {}
haRegex = re.compile(r'(Ha){3}')#you can set a min or max with {3,5} , if any of those numbers
#is left blank would mean inf min or max respectively
mo1 = haRegex.search('HaHaHaHaHa')
mo2 = haRegex.search('Ha')#it doesn't match the amount specified
print(mo1.group(), str(mo2))

#regex in Python are by default greedy, they will always match the longest
greedyRegex = re.compile(r'(Ha){3,5}')
lazyRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyRegex.search('HaHaHaHaHa')
mo2 = lazyRegex.search('HaHaHaHaHa')
print(mo1.group(), mo2.group())