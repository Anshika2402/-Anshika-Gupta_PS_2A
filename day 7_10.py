''' Character by character frequency count 

s=input('Enter a string: ')
c={}
for i in s:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print('Frequency of each character in string: ',s,'is --->>')
print(str(c))

for i in s:
    x=s.count(i)
    print('Count of ',i,' is: ',x)
'''

s=input('Enter a string: ')
r=''
for i in s:
    if i not in r:
        print('Count of ',i,'is: ',s.count(i))
        r=r+i
