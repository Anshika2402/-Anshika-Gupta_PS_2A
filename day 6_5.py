#Matrix in spiral form

r=int(input("Enter the no. of rows:")) #4
c=int(input("Enter the no. of columns:")) #4
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
print('\n')
x=0
y=0
p=r
q=c
while (x<p and y<q):
    for i in range (y,q): #0,4= 0,1,2,3
        print(m[x][i],end=' ') #0,0 0,1 0,2 0,3 first row
    x+=1 #11
    for i in range(x,p): #1,4= 1,2,3
        print(m[i][q-1],end=' ') #1,3 2,3 3,3 last column
    q-=1 #3
    if (x<p):
        for i in range(q-1,y-1,-1): #2,-1,-1= 2,1,0
            print(m[p-1][i],end=' ') #3,2 3,1 3,0 last row
        p-=1 #3
    if (y<q):
        for i in range(p-1,x-1,-1): #2,-1,-1= 2,1,0
            print(m[i][y],end=' ') #2,0 1,0 0,0 first column
        y+=1

        
    
        
    
