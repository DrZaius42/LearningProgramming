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


#learning to use the findall() method

phoneNumRegex = re.compile(r'(\d){3}-(\d){3}-(\d){4}')
mo = phoneNumRegex.search('Cell: 415-555-9999, Work: 212-555-0000')
print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000')
print(mo)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000')
print(mo)


#character classes
xmasRegex = re.compile(r'\d+\s\w+')
testRegex = re.compile(r'\d+\s\w')#should match digit-space-one letter
mo1 = xmasRegex.findall('12 drummers, 11 pipers, 10 lord, 9 ladies,'
                        '8 maids, 7 swans, 6 geese, 5 rings, 4 birds,'
                        '3 hens, 2 doves, 1 partridge')

mo2 = testRegex.findall('12 drummers, 11 pipers, 10 lord, 9 ladies,'
                        '8 maids, 7 swans, 6 geese, 5 rings, 4 birds,'
                        '3 hens, 2 doves, 1 partridge')

print(mo1)                        
print(mo2)#it worked as I spected


#custom character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

#by adding ^ just after opening [] you make a negative character class
consonantRegex = re.compile(r'[^aeiouAEIOU ]')
mo = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo)

#"Carrots cost dollars" caret(^) at the beginning, dollar($) at the end
#^ must start with
#$ must end with
endsWithNumber = re.compile(r'\d$')
yourNumber = endsWithNumber.search('Your number is 42')
print(yourNumber)

wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('12345567890')
mo2 = wholeStringIsNum.search('123125asfd987')
print(mo.group())
print(mo2)#matches None, as expected, because of the letters in the middle


#wildcart character the dot (.)
#matches any character except newline
atRegex = re.compile(r'.at')#(r'.at|\w.at')this fixes the pattern for flat
#since there's only one dot the pattern matches "lat" instead of "flat"
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

#matching everything with .*
#. matches any character
#* matches zero or more characters
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Sebastian Last Name: Olivares')
print(mo.group(1))
print(mo.group(2))

#.* nongreedy mode
nongreedyRegex = re.compile(r'<.*?>')
greedyRegex = re.compile(r'<.*>')
mo1 = nongreedyRegex.search('<To serve man> for dinner.>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())
print(mo2.group())

#matching newlines with the dot character
newlineRegex = re.compile(r'.*', re.DOTALL)
mo1 = newlineRegex.search('Serve the public trust.\nProtect the innocent.')
print(mo1.group())

#case-insensitive matching
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoBocoP')
print(mo.group())

#verbose mode
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code
    (\s|-|\.)?          #separator
    \d{3}               #first 3 digits
    (\s|-|\.)           #separator
    \d{4}               #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #extension
    )''', re.VERBOSE)

numberCommas = re.compile(r'^\d{1,3}(,\d{3})*$')
mo = numberCommas.search('2,343,232')
print(mo.group())