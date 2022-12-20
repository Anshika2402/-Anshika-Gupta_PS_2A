def stat():
    l=[10, 2, 30, 4, 45]
    n=len(l)
    s=sum(l)
    x=s/n
    print("Mean is: "+str(x))
    l.sort() 
    if n%2==0:
        m1=l[n//2]
        m2=l[n//2-1]
        m=(m1+m2)/2
    else:
        m=l[n//2]
    print("Median is: "+str(m))
stat()
