''' Balanced number 123330=> 1+2+3=6=3+3+0 '''

n=input('Enter a number: ')
size=len(n) #6
left=0
right=0
for i in range(0,int(size/2)): #0,3= 0,1,2
    left+=int(n[i]) #1+2+3=6
    right+=int(n[size-i-1]) #6-0-1=5, 6-1-1=4, 6-2-1=3 ---> 0+3+3=6
if left==right:
    print('It is a balanced number. ')
else:
    print('It is not a balanced number. ')
