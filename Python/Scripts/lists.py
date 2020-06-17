import random

l = [123,'abc',3.1415]
print(len(l))
print(l[1])
g = ['a',2,'otra'] + l
print(l)
#l.append('NI')
print(l)
l.insert(1, 99)
a = l.pop(3)#requires the position to pop
l.remove('abc')
l.sort()
print(l)
M = [[1,2,3],[4,5,6],[7,8,9]]#this could represent a matrix
print(M[2])#this prints the third element of M, the row [7,8,9] in this case
print(M[2][1])#this prints the second element of the third row
col2 = [row[1] for row in M]#gets the second element of every row forming the second column
print(col2)
row2 = [col[0] for col in M]#gets the first element of every column formin the first row
print(row2)
diag = [M[i][i] for i in [0,1,2]]#gets the diagonal of a matrix
print(diag)
s = 'spam'
doubles = [c * 2 for c in s]
print(doubles)

myList = list(range(0,5))#makes a list of int from 0 to 4
print(myList)
myList = list(range(-6,7,2))#makes a list of int from -6 to 6 with a step of 2
print(myList)

#comprehension syntax
print({sum(row) for row in M})#this makes a set of the sum of every row in the matrix M
print({i:sum(M[i]) for i in range(0,3)})

"""
#using the enumerate() method returns an index and the idexed item from a list
b = ['a', 'b', 2, 20, ['spam', 'eggs']]
print(list(enumerate(b)))
print(random.choice(b))
print('before shuffle', b)
random.shuffle(b)
print('after shuffle', b)
"""