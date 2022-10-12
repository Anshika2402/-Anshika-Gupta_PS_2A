x=int(input('Enter value of X: '))
y=int(input('Enter value of Y: '))
if x>0 and y>0:
    print('1st quad.')
elif x<0 and y>0:
    print('2nd quad.')
elif x<0 and y<0:
    print('3rd quad.')
elif x>0 and y<0:
    print('4th quad.')
elif x==0 and y==0:
    print('Origin.')

