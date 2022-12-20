def term(n): #6
    if n<=2:
        return (n-1)
    else:
        return term(n-1)+term(n-2) #t5+t4=t4+t3+t3+t2=...
n=int(input('Enter n: '))
print(term(n))

#0 1 1 2 3 5 8 13 21 ....
