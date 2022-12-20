def arm():
     x=int(input("Enter lower limit: "))
     y=int(input("Enter upper limit: "))
     print("Armstrong numbers are: ")
     sum=0
     for i in range(x,y+1):
          m=i
          while m>0:
               n=m%10
               sum+=n**m
               n=n//10
     if i==sum:
          print(i)
arm()
