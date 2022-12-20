''' Check for palindrome in a string '''
s=input('Enter a string: ')
r=''
for i in range(len(s)):
    x=list(s)
l=x[::-1]
for j in l:
    r+=j
if s==r:
    print(s,'is a palindrome.')
else:
    print(s,'is not a palindrome.')
