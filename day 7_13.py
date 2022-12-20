''' Sort city names '''

s=input('Enter a string: ')
l=[]
r=''
for i in s.split():
    l.append(i)
l.sort()
for al in l:
    r+=al+' '
print('New sorted string: ',r)
