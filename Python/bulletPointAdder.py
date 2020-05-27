#usr/bin/python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard
import  pyperclip, sys

text = pyperclip.paste()
lines = text.split('\n') 

#separate lines and add stars
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] 

text = '\n'.join(lines)
pyperclip.copy(text)