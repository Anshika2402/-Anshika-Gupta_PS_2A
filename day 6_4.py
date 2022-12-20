'''
import numpy as np
x=np.array([[1,2],[3,4],[5,6]])
print(x,'\n')
print(np.rot90(x,2))

1 2 3   9 8 7
4 5 6 = 6 5 4
7 8 9   3 2 1
'''

r=int(input("Enter the no. of rows:")) 
c=int(input("Enter the no. of columns:")) 
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
for i in range(n//2):  #1
    for j in range(n):  #0
        x=m[i][j]  
        m[i][j]=m[n-i-1][n-j-1]
        m[n-i-1][n-j-1]=x
if (n%2==1):  #3 true
    for j in range(n//2): #1
        x=m[n//2][j]  #1,0
        m[n//2][j]=m[n//2][n-j-1]  #1,1
        m[n//2][n-j-1]=x 
print('Matrix rotated by 180 anti-clockwise: ')
for i in range(r):
    for j in range(c):
        print(m[i][j], end=" ")
    print()   
        
        
        
    
