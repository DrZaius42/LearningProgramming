#! usr/bin/python3
#mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'hello there': """General Kenobi!!""",
        'science': """you know, I'm something of a scientist myself."""}


import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
    """print('Do you want to add it? yes/no')
    addNew = input()
    if addNew.lower() == 'yes':
        print('Type your new text: ')
        newText = input()
        TEXT.update({keyphrase : newText})
        print('Your new keyphrase has been added.')
        print(TEXT)
    else:
        sys.exit()"""