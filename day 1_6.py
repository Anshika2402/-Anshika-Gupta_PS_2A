a=int(input('Enter length of side 1:'))
b=int(input('Enter length of side 2:'))
c=int(input('Enter length of side 3:'))
if (a==b) and (b==c) and (c==a):
    print('Equilateral.')
elif (a==b) or (b==c) or (c==a):
    print('Isosceles.')
else:
    print('Scalene.')
    
