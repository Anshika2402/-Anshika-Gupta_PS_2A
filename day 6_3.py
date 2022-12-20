'''
6 7 2
1 5 9
8 3 4
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
n=len(m)
s1,s2=0,0
for i in range(n): #3= 0,1,2
    s1+=m[i][i] #0,0  1,1   2,2
    s2+=m[i][n-i-1] #0,0   0,1   0,2
for i in range(n):
    srow,scol=0,0
    for j in range(n):
        srow+=m[i][j] #0,0   0,1   0,2
        scol+=m[j][i] #0,0   1,0   2,0
if (s1==s2==srow==scol):
    print("It is a magic matrix.")
else:
    print("It is not a magic matrix.") 
        
