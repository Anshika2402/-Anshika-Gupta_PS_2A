''' Change case in a string '''

s=input('Enter a string: ')

'''
r=s.swapcase()
print('Resultant string: ',r)
'''

r=''
for i in range(len(s)):
    if (s[i]>='a' and s[i]<='z'):
        r+=chr((ord(s[i])-32))
    elif (s[i]>='A' and s[i]<='Z'):
        r+=chr((ord(s[i])+32))
    else:
        r+=s[i]
print('Original string: ',s)
print('Resultant string: ',r)
