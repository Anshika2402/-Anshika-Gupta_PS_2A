'''Repeatedly split and add numbers till left with 1 digit
98= 9+8= 17= 1+7= 8'''

n=int(input('Enter a number: '))
sum=0
while (n>0 or sum>9): #98
    if n==0: 
        n=sum
        sum=0
    sum+=n%10 #8 ; 8+9 = 17 ; 7 ; 8
    n//=10 #9 ; 0 ; 1 ; 0
print('Sum: ',sum)

    
    
    
