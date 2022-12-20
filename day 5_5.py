n=int(input('Enter the limit: '))
arr1=list(range(1,n+1,2))
arr2=list(range(2,n+1,2)) #n,1,-2= 10,8,6,4,2
arr2.reverse()
print(arr1,arr2)
