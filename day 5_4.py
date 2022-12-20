def absdiff():
    l=eval(input('Enter elements: '))
    k=int(input("Enter k: "))
    arr=list(l) #7,98,56,43,45,23,12,8
    n=len(arr) #8
    i,f=0,0
    l1=[]
    while i<n: #0 to n-1=7
        if arr[i]<k and arr[i]>9: #9<arr[i]<54
            x=arr[i] #assign position
            while x>9: #43,45,23,12        
                r=x%10  #3,5,3,2  
                x=x//10  #4,4,2,1  
                c=x%10   #0,0,0,0
                if abs(r-c)!=1: #3,5,3,2
                    f=1
                    break
            if f==0: #-1,1,1,1
                l1.append(arr[i]) 
            f=0
        i+=1
    print(l1)
absdiff()
