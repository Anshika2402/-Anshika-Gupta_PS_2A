import math
def sin(x,n):
    s=0
    for i in range(n):
        m=(-1)**i
        pi = 22/7
        y=x*(pi/180)
        s+=((y**(2.0*i+1))/math.factorial(2*i+1))*m
    return s
x=int(input("Enter value of x: "))
n=int(input("Enter no. of terms: "))
print(round(sin(x,n),2))
