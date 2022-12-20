arr=eval(input('Enter list: '))
l=list(arr)
n=len(arr) #0,1,2,3
s1,s2=0,0
for i in range(0,n//2): #0,1
    s1+=l[i]
print(s1)
for j in range(n//2,n): #2,3
    s2+=l[j]
print(s2)
print(s1*s2)
