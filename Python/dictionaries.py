import pprint

d = {}#this creates an empty dictionary
d['name'] = 'Sebastian'
d['job'] = 'student'
d['age'] = 21
print(d)
print(d['name'])
seb1 = dict(name='Sebastian', job='student', age=21)#keyword arguments syntax way to create a dictionary using the type "dict"
print(seb1)
seb2 = dict(zip(['name','job','age'],['Sebastian','student','21']))#zipping syntax creates a dictionary with to lists of objects
print(seb2)
#nesting structures
rec = {'name': {'first': 'Sebastian', 'last': 'Olivares'},
    'job': ['student', 'gamer', 'memelord'],
    'age': 21 + 5/12}
print(rec)
if 'weight'not in rec:
    print('missing category') 
#sorting keys of a dictionary
numbers = {1: 'a', 2: 'b', 3: 'c' }
ks = list(numbers.keys())
ks.sort()
for key in ks:
    print(ks[key - 1], '=>', numbers[ks[key - 1]])

print(numbers.get(1, 0))
print(numbers.get(4, 0))
numbers.setdefault(6, 'f')
print(numbers)

spam = {'cat': 42}
print('cat' in spam and'cat' in spam.keys())
print('cat' in spam and 'cat' in spam.values())
spam.setdefault('aaa', 'black')
pprint.pprint(spam)