f=1
sum=0
n=int(input('Enter limit: '))
for i in range(1,n+1):
    f*=i
    sum+=f
print('Sum: ',sum)
