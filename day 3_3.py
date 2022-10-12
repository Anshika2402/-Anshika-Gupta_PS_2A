f=1
sum=0
n=int(input("Enter Limit: "))
x=int(input("Enter value of x: "))
for i in range (1,n+1):
    f*=i
    sum+=(1+(x**i/f))
print('Final sum is: ',sum)
