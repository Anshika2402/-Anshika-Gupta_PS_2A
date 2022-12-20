x=input('Enter string1: ')
y=input('Enter string2: ')
r=''
for i in y:
    if i not in x:
        x=x.replace(i,'')
print('New string: ',x)
