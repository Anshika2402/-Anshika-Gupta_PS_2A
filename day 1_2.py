a=int(input('Enter 1st no.: '))
b=int(input('Enter 2nd no.: '))
c=int(input('Enter 3rd no.: '))
if (a>b):
    if (a>c):
        print(a,'is greatest.')
    else:
        print(c,'is greatest.')
elif (b>c):
    print(b,'is greatest.')
else:
    print(c,'is greatest.')
