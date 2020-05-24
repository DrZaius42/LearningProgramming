def commaJoiner(elements):#joins a list of elements in a single string adding an "and" before the last one.
    joinedElements = ""
    if elements == []:
        print('Please enter a valid list.')
        return None

    for i in elements:
        if elements.index(i) == len(elements) - 1:
            joinedElements += 'and ' + str(i)
        
        else:
            joinedElements += str(i) + ', '
    
    return joinedElements

spam = [1, 2, 3, 4]
print(commaJoiner([]))

