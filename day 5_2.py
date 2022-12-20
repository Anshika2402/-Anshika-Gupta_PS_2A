l=eval(input('Enter size of candles: '))
arr=list(l)
n=len(arr)
max=arr[0]
for i in range (n):
    if arr[i]>max:
        max=arr[i]
print(max)
