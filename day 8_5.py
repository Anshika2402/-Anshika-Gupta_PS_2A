''' Least prime factors of N '''

n=int(input('Enter a number: '))
l,r=[],[]
for i in range(1,n+1): #1,7 =1,2,3,4,5,6
    for j in range(2,int(i**0.5)+1): #2,2 2,2 2,2 2,3 2,3 2,3
        if i%j==0:
            break
    else:
        l.append(i)
print('Prime numbers below',n,': ',l)
for i in range(len(l)):
    if n%l[i]==0:
        r.append(l[i])
print('Prime numbers which are factors of',n,': ',r)
        
