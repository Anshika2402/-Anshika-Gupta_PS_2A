n=int(input("Enter limit: "))
sum=0
for i in range(1,n+1):
    sum+=(i*(i+1)*(i+2))
print("Sum: ",sum)
