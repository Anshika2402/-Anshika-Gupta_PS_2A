def prime():
    x=int(input('Enter lower limit: '))
    y=int(input('Enter upper limit: '))
    l=[]
    for i in range(x,y+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            l.append(i)
    print(l)
prime()
