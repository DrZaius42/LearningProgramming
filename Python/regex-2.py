#learning to use the findall() method
import re

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