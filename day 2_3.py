n=int(input("Enter limit: "))
a=65  #97 for a
for i in range(1,n+1):
    for j in range(1,i+1):
        print("%c" %(a), end="")
    a+=1
    print()
