f = open('data.txt','w')#this creates an empty text file
f.write('Hello World!!\n')
f.write("How ya'll been doing?\n")
f.close()
a = open('data.txt','r')
text = a.read()
print(text)#prints interprets control characters
b = text.split('\n')
print(b)

for line in open('data.txt'):#this is another way to work with a text file
    print(line)