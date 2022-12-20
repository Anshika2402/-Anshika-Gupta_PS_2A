def exp(a,b): #3,5
    if (b==0):
        return 1 #raised to 0=1
    elif (int(b%2)==0): #5%2==1
        return (exp(a,int(b/2))*exp(a,int(b/2)))
    else:
        return (a*exp(a,int(b/2))*exp(a,int(b/2))) #3*exp(3,2)*exp(3,2)= 3*exp(3,1)*exp(3,1)*exp(3,1)*exp(3,1)= 3*3* repeats 5 times, *exp(3,0) repeats 5 times and returns 1= 3**5=243
a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
print(exp(a,b))
