n=int(input('Enter limit: '))
k=0
for i in range(1,n+1):
    for j in range(0,i):
        k+=1;
        print(k,end=" ")
    print()
