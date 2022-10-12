n=int(input('Enter limit: '))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
