c=int(input('Enter temperature: '))
if c<0:
    print('Freezing weather.')
elif c>0 and c<10:
    print('Very cold.')
elif c>10 and c<20:
    print('Cold.')
elif c>20 and c<30:
    print('Normal.')
elif c>30 and c<40:
    print('Hot.')
else:
    print('Very Hot.')
