#this is a file to count the number of characters in a string
#using the method dictionary.setdefault()
import pprint

message = 'It was a bright cold day in April, an the clocks were striking thirteen.'
count = {}#creates the empty dictioanry count

for character in message:
    count.setdefault(character, 0)#adds each new character to the dictionary as a key with value zero
    count[character] = count[character] + 1#if a character is already in the dict, the value is aumented by 1, indexing with the character itself

pprint.pprint(count)