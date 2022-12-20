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

    
    
    
    
