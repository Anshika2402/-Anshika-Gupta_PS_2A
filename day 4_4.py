def perf_num(n):  
   if n<1:
      return False
   sum=0
   for i in range(1,n):
      if n%i==0:
         sum+=i
   return sum==n
minv=int(input('Enter minimum value: '))
maxv=int(input('Enter maximum value: '))
print('Perfect numbers from %d to %d are:' %(minv, maxv))
for i in range(minv, maxv+1):
   if perf_num(i):
      print(i,end=', ')
