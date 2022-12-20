''' Character by character frequency count '''

s=input('Enter a string: ')
r=''
for i in s:
    if i not in r:
        print('Count of ',i,'is: ',s.count(i))
        r=r+i
