#Self Dividing numbers

def selfdivnum():
    res=[]
    for n in range(left,right+1):
        num=n 
        c=True
        while num>0:
            mod=num%10
            if mod==0 or n%mod!=0:
                c=False
                break
            num//=10
        if c==True:
            res.append(n)
    print(res)
left=int(input('Enter lower limit: '))
right=int(input('Enter upper limit: '))
selfdivnum()





'''
l=list(range(left,right+1))
r,p=[],[]
for n in l:
    for i in str(n):
        if i!='0':
            if n%int(i)==0:
                r.append(n)
for x in r:
    if x not in p:
        p.append(x)
print(p)
        
''' 

    
    
    
    
