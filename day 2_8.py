n=int(input('Enter limit: '))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end='')
    for j in range(i,0,-1):
        print('*',end='')
    for j in range(2,i+1):
        print('*',end='')
    print()
