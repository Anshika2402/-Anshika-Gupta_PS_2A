n=int(input("Enter limit: "))
s=""
print("\nStar Z Pattern: ")
for i in range (0,n):
    for j in range (0,n):
        if (((i==0 or i==n-1) or (i+j)==(n-1))):
            s+="*"
        else:
            s+=" "
    s+="\n"
print(s)
