def tail_fact(n,a=1):
    if (n==0):
        return a
    return tail_fact(n-1,n*a)
n=int(input("Enter limit: "))
print(tail_fact(n))
