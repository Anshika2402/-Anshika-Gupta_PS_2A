''' nth term of series
9,33,73,129,...
24, 24+16=40, 40+16=56 '''

n=int(input('Enter a no: ')) 
start=9
sum=24
for i in range(1,n): 
    start+=sum
    sum+=16
print(start)
