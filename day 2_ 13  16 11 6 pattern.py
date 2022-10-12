l=[]
n=16
m=n
l.append(m)
while (m>0):
    m-=5
    l.append(m)
while (m<n):
    m+=5
    l.append(m)
print(*l)
