#! /usr/bin/python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?  #area code 
    (\s|-|\.)?          #separator 
    (\d{3})             #first 3 digits
    (\s|-|\.)           #separator 
    (\d{4})             #last 4 digits 
    (\s*ext|\s*x|\s*ext.)?    #extension prefix
    (\s*\d{2,5})?        #extension number
    ''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     #username
    @                     #@ symbol
    [a-zA-Z0-9.-]+        #domain name
    \.[a-zA-Z]{2,4}     #dot something
    )''', re.VERBOSE) 
text = pyperclip.paste()
moPhones = phoneRegex.findall(text)#matches regex phone in text
moEmail = emailRegex.findall(text)#matches regex emails in text

text = str(pyperclip.paste())
matches = []
for groups in moPhones:
    if groups[0] != '':
        phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    else:
        phoneNum = '-'.join([groups[2], groups[4]])
    if groups[5] != '':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)

for email in moEmail:
    matches.append(email)

#copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print(pyperclip.paste())

else:
    print('No phone numbers or email addresses were found.')