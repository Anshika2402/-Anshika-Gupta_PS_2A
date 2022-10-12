f=1
a,b,c=0,0,0
n=int(input("Enter Limit: "))
for i in range (1,n+1):
    f*=i
    if (i%2!=0):
        a+=(i/f)
    else:
        b+=(i/f)
    c=a-b
print('Final sum is: ',c)
