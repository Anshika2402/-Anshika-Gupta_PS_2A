a=eval(input("Enter elements for list 1: "))
b=eval(input("Enter elements for list 2: "))
l1=list(a)
l2=list(b)
r1,r2=[],[]
for i in l1:
    for j in l2:
        if i==j:
            r1.append(i)
for m in l1:
    if m not in l2:
        r2.append(m)
for n in l2:
    if n not in l1:
        r2.append(n)
print('Elements in both lists: ',r1)
print('Elements that are not in both lists: ',r2)
