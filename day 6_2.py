'''
import numpy as np
x=np.array([[1,2],[3,4],[5,6]])
print(x)
print(np.rot90(x,1))

1 2 3     3 6 9
4 5 6  =  2 5 8
7 8 9     1 4 7
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
for row in m:
    row.reverse()
n=len(m)
for i in range(n): 
    for j in range(i):
        m[i][j],m[j][i]=m[j][i],m[i][j]
print('Matrix rotated by 90 anti-clockwise: ')
for i in range(r):
    for j in range(c):
        print(m[i][j], end=" ")
    print()
