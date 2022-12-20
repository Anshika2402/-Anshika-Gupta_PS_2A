l=eval(input('Enter elements: '))
arr=list(l)
l1=[]
for i in arr:
    if arr.count(i)<2:
        l1.append(i)
print('List with elements which do not repeat: ',l1)
