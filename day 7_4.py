''' Word count in a string '''
s=input('Enter a string: ')
a=s.lower()
b=a.split()
c=0
for i in range(len(b)):
    c+=1
print('Word count: ',c)
