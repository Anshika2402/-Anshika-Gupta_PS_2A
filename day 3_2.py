fact=1
sum=0
x=int(input("Enter Limit: "))
for i in range (1,x+1):
    fact*=i
    sum+=(fact/i)
print('Final sum is: ',sum)
