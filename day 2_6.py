n=int(input('Enter limit: '))
x=1
s=n-1
for j in range(1,n+1) :
	x=j
	for i in range(1,s+1) :
	    print(" ", end="")
	s=s-1
	for i in range(1,j+1) :
	    print(x,end="")
	    x=x+1
	x=x-2
	for i in range(1,j):
	    print(x,end="")
	    x=x-1
	print()

