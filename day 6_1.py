'''
import numpy as np
x=np.array([[1,2],[3,4],[5,6]])
print(np.rot90(x,3))

1 2 3   7 4 1
4 5 6 = 8 5 2
7 8 9   9 6 3
'''

r=int(input("Enter the no. of rows:")) #3
c=int(input("Enter the no. of columns:")) #3
m=[]
print("Enter the elements :") 
for i in range(r):  
    a=[] 
    for j in range(c):       
         a.append(int(input())) 
    m.append(a)
print('Input Matrix: ')
for i in range(r):  
    for j in range(c):   
        print(m[i][j], end=" ")  
    print()
n=len(m)  #3
for i in range(n):  #3= 0,1,2
    for j in range(i):  #2= 0,1
        m[j][i],m[i][j]=m[i][j],m[j][i] #3,0 becomes 0,3 
print('Matrix rotated by 90 clockwise: ')
for row in m:
    row.reverse()   #1,4,7 on top becomes 7,4,1
for i in range(r):
    for j in range(c):
        print(m[i][j], end=" ")
    print()

'''
n=len(m[0]) #3
for i in range(n//2): #n//2=1 ; 0,1
    for j in range(i,n-i-1): #0,[3-0-1=2 ; 3-1-1=1] 0,1..2
        x=m[i][j] #1
        m[i][j]=m[n-1-j][i] #1=
        m[n-1-j][i]=m[n-1-i][n-1-j]
        m[n-1-i][n-1-j]=m[j][n-1-i]
        m[j][n-1-i]=x
n=len(m[0])
print('Matrix rotated by 90: ')
for i in range(r):
    for j in range(c):
        print(m[i][j], end=" ")
    print()
'''
