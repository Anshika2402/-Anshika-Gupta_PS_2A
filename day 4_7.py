f=[1,1,2,6,24,120,720,5040,40320,362880]
def strong(n):
    no=str(n)
    sum=0
    for i in range(len(no)):
        sum+=f[ord(no[i])-ord('0')]
    if sum==n:
        return True
    else:
        return False
def disp(n):
    for i in range(1,n+1):
        if (strong(i)):
            print(i,end=" ")
n=int(input('Enter a limit: '))
disp(n)
