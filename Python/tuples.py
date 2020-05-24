#immutable sequence
t = (1,2,3,4)
print('the whole tuple is: ', t)
print('the value in position 2 is:', t[2])#can be indexed
a = (5,4)
t = a + t#can be concatenated
print('after concatenation: ', str(t))
print('the index for 5 is: ', t.index(5))#the method .index() returns the index of an element in the tuple
print('the number of times 4 is repeated in the tuple is: ', t.count(4))#the method .count() returns the number of times the element is in the tuple