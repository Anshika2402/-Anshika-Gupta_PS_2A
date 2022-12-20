''' Roots of a quadratic equation
ax^2+bx+c=0
r= (-b +- (b^2-4ac)^1/2)/2a '''


a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
c=int(input('Enter the value of c: '))
d=(b**2)-(4*a*c)
r1=(-b+(d**0.5))/(2*a)
r2=(-b-(d**0.5))/(2*a)
print('Roots: ',r1,' ',r2)

