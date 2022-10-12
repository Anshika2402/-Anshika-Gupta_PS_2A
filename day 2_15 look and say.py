n=int(input("Enter nth term: "))
i=0
while i<n:
    if i==0:
        a=[1]
    else:
        c=1
        l=[]
        for j in range(1,len(a)):
            if a[j]==a[j-1]:
                c+=1
            else:
                l+=[c,a[j-1]]
                c=1
        l+=[c,a[len(a)-1]]
        a=l
    i+=1
    print(*a)
