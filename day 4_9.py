def gcd(x,y):
    if (y==0):
        return x
    else:
        return gcd(y,x%y)
def lcm(x,y):
    return(x*y)
n1=int(input('Enter 1st number: '))
n2=int(input('Enter 2nd number: '))
print('LCM of',n1,'and',n2,'is: ',lcm(n1,n2))
