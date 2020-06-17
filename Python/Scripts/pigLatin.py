#English to Pig Latin
#if a word begins with a vowel the word yay is added to the end of it.
#if a word begins with a consonant that consonant is moved to the end and the word ay is added.


print('Enter a message in English to translate to Pig Latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = []#the word of the message in pig latin
for word in message.split():
    #separate the non-letters at the beginning of the word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    
    if len(word) == 0:#checks out True if the word had no letters
        pigLatin.append(prefixNonLetters)
        continue#continues with the next iteration of the for in line 11

    #separate the non-letters at the ending of the word
    sufixNonLetters = ''
    while not word[-1].isalpha():
        sufixNonLetters += word[-1]
        word = word[:-1]
    
    #remeber if the word was title or upper cased
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()#make the word lowercase for translation

    #separate the consonants at the start of the word
    prefixConsonants = ''
    while not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    
    #add the pig latin ending to the word
    if prefixConsonants == '':
        word += 'yay'
    else:
        word += prefixConsonants + 'ay'
    
    #sets the word back to upper or title case
    if wasTitle:
        word = word.title()
    if wasUpper:
        word = word.upper()
    
    #adds the prefix and sufix non-letters
    pigLatin.append(prefixNonLetters + word + sufixNonLetters)

#joins all the words back into a single string
pigLatin = ' '.join(pigLatin)
print(pigLatin)
