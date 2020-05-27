#this is a script for testing strings operations

a = 'spam'
print(len(a))
print(a[0])
print('this a[-1] is equivalent to this a[len[a]-1]')
print('a[-1] : ' + a[-1])
print('a[len(a)-1]: ' + a[len(a)-1])
print(a[:-2])
print(a*8)
a = 'h' + a[1:]
print(a)
b = 'paralelepipedo'
print(b.find('para'))
print(b.find('pare'))
print(b.replace('para','PARA'))
print(b)
line = 'aaa,bbb,ccc,ddd'
print(line)
line = line.split(',')
print('this is after split: ',line)
line = '-'.join(line)
print('this is after join: ',line)

groceryList = """ apples
mayo
tomatoes
pepsi"""

groceries = groceryList.split('\n')#splits the string by the separator but doesn't icludes it
print(groceries)
print('Hello, world!!'.partition('w'))#splits the string in 3, (before, separator, after)
print('Hello, world!!'.partition('o'))#cuts at the first apearence of the separator
print('Hello, world!!'.partition('xyz'))#if the separator is not on the string the last two parts are empty on the return
before, sep, after = 'Hello, world!!'.partition(' ')#obatining the 3 parts using the multiple assigning trick


#using rjust(), ljust() and center()
print('Hello'.rjust(10))
print('Hello'.ljust(20))
print('Hola'.rjust(10, '*'))

count = 0
for character in ('Hello'.center(20)):
    if character != 'H':
        count += 1
    else:
        break
print(count)

#using strip() removes whitespace
spam = '    Hello, world   '
print(spam.strip())
print(spam.rstrip())
print(spam.lstrip())