'''Suffixes of string'''

s=input('Enter a string: ')
n=len(s)
l=[]
c=0
for i in range(1,n):
    l.append(s[-i:])
print(l)
for i in l:
    c+=1
print('No. of suffixes of string: ',c)

