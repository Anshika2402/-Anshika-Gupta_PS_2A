n=int(input('Enter limit: '))
k=0
for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j>i):
            print(" ",end="")
        else:
            k+=1
            print(k,end=" ")
    print()
