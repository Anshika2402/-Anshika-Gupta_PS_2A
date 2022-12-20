''' Two no. A & B, find Kth digit from right of A to power B '''

a=int(input('Enter the value of A: ')) #4
b=int(input('Enter the value of B: ')) #5
k=int(input("Enter K: ")) #2
exp=a**b #1024
c=0
print('\nA^B= ',exp)
while (exp>0 and c<k): #1024>0 and 0,1<2
    r=exp%10 #4 ; 2.40
    c=c+1 #0---1
    if c==k: #1---2
        print('Kth digit from right of A to power B: ',int(r)) #int 2.40= 2
    exp=exp/10 #102.4 ; 10.24
