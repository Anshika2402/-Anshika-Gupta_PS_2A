#Cats and Mouse
def cm(x,y,z):
    cA=abs(x-z)
    cB=abs(y-z)
    if (cA<cB):
        return 'cat A'
    elif (cB<cA):
        return 'cat B'
    else:
        return 'mouse C'
x=int(input('Enter x: '))
y=int(input('Enter y: '))
z=int(input('Enter z: '))
print(cm(x,y,z))
