'''Prefixes of string'''

s=input('Enter a string: ')
n=len(s)
c=0
l=[]
for i in range(1,n):
    l.append(s[:i])
print(l)
for i in l:
    c+=1
print('No. of prefixes of string: ',c)
























