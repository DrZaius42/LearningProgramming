#this script is for testing input validation schemes

while True:
    print('Enter your age: ')
    age = input()
    try:
        age = int(age)#converts to int since input() returns a string
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}')#f at the beginning for formatted text

#this becomes tedious for every kind of input
#it could also allow to exploits

#PyInputPlus is a library for easy input validation
import pyinputplus as pyip
response = pyip.inputNum(prompt='Enter a number: ')
print(response)
response = pyip.inputInt(prompt= 'Enter a integer: ')
print(response)


response = pyip.inputNum('Min number: ', min=4)
print(response)
response = pyip.inputNum('GreaterThan: ', greaterThan=4)
print(response, ' is greater than 4')
response = pyip.inputNum('In a range: ', min=4, lessThan=6)
print(response)
#for optional input you can set pyip.inputNum(blanck=True)

#for limit the number of tries or the amount of tyme
response = pyip.inputNum(prompt='Testing limit parameter:',
                        limit=2, default='Failed to enter a valid number.')
#it shows the "default" message instead of displaying the error
response = pyip.inputNum(prompt='Testing timeout', timeout=10)

#specifying with regex
print('Enter a roman number: ')
response = pyip.inputNum(allowRegexes=[r'(I|V|X|M|L|C|D])+', r'(i|v|x|m|l|c|d)+'
                        ,r'zero'])
#you have to pass a list of the regexes to allow
#the regex accepts the letters in any order and zero
#xvx is a valid input, but not a valid roman number, the regex accepts it anyway
#you can do the same in lowercase roman numbers

response = pyip.inputNum(prompt='Enter a number: ', blockRegexes=[r'[02468]$'])
#this blocks any even number
