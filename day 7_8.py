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



'''
beg,end=0,0
while beg<n:
    if s[end]==s[end-beg]:
        print(s[beg:end+1],end=' ')
        end+=1
        if end==n:
            beg+=1
            end=beg
    else:
        beg+=1
        end=beg


print([s[:i] for i in range(1,n)])
 '''



















































