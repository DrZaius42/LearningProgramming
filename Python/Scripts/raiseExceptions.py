
raise Exception('This is the error message.')

#assertions

ages = [26, 57 ,68, 12, 29, 99]
ages.sort()
assert ages[0] <= ages[-1]

ages.reverse()
assert ages[0] <= ages[-1]