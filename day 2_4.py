n=int(input("Enter limit: "))
a=64  #97 for a
for i in range(1,n+1):
    for j in range(0,i):
        a+=1
        print("%c" %(a), end=" ")
    print()
