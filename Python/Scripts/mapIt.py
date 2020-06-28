#! /usr/bin/env python3
#   mapIt.py - Opens addresses on google maps from clipboard or cli
import sys, webbrowser, pyperclip
#get a street address from cli or clipboard
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
#open browser to the google maps page
webbrowser.open('https://www.google.com/maps/place/' + address)

