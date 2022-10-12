bs=float(input("Enter basic salary: "))
g=input("Enter grade: ")
hra=0.20*bs
da=0.5*bs
pf=0.11*bs
if (g=='a'):
    a=1700
elif (g=='b'):
    a=1500
else:
    a=1300
ts=bs+hra+da+a-pf
print('Total Salary:',int(ts))
    
