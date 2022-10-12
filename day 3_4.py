f=1
a,b,c=0,0,0
n=int(input("Enter Limit: "))
x=int(input("Enter value of x: "))
for i in range (1,n+1):
    f*=i
    if (i%2==0):
        a+=(x**i/f)
    else:
        b+=(x**i/f)
    c=1+a-b
print('Final sum is: ',c)
