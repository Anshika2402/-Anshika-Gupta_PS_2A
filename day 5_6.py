#[1,2,3,4,5,6] = [2,1,4,3,6,5] 

x=eval(input('Enter list: '))
l=list(x)
n=len(l)
if n%2==0:
    for i in range(0,n,2): #0,6,2= 0,2,4
        l[i],l[i+1]=l[i+1],l[i] #0,1=1,0   2,3=3,2
else:
    for i in range(0,n-1,2):
        print(i)
        l[i],l[i+1]=l[i+1],l[i]
print('Final list: ',l)
