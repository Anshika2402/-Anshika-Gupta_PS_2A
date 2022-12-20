'''Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.'''

def trailzeros():
    n=int(input("Enter no.: "))
    f=1
    if n==0:
        print(1)
    else:
        for i in range(1,n+1):
            f=f*i
        print(f)
    c=0
    while f%10==0:
        f=f//10
        c+=1
    print('Count of trailing zeroes: ',c)
trailzeros()

