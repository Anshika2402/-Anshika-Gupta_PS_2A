def gcd(x,y):
    if (y==0):
        return x
    else:
        return gcd(y,x%y)
x=int(input('Enter 1st number: '))
y=int(input('Enter 2nd number: '))
r=gcd(x,y)
print('GCD is: ',r)
