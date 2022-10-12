import math
def l(x,n):
    sum=1
    term=1
    y=2
    for i in range(1,n):
        fct=1
        for j in range(1,y+1):
            fct=fct*j
        term=term*(-1)
        m=term*math.pow(x,y)/fct
        sum+=m
        y+=2
    return sum
x=int(input("Enter value of x: "))
n=int(input("Enter no. of terms: "))
print('%.4f'% l(x, n))
