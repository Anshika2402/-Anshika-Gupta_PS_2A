'''
33333
32223
32123
32223
33333
'''

x=100
n=int(input('Enter number: '))
#for limit 3, we have 5 rows and columns
s=n*2-1 #3*2-1=5
#a is 0 to check each row, matrix. n is printed on 1st r,c.
a=0
b=s-1 #5-1=4
y=[[0 for i in range(x)]for i in range(x)] #initialising matrix space
while (n>0):
    for i in range(a,b+1): #loop from 0 to b=4
        for j in range(a,b+1): 
            if (i==a or i==b or j==a or j==b): #if a=0,1,2,3==i=0,1,2,3 print n
                y[i][j]=n #treating pattern as matrix
    a+=1 #loop increment
    b-=1 #values moving back
    n-=1 #final print values decrease inside
for i in range(s):  
    for j in range(s): 
        print(y[i][j], end = '') 
    print()
