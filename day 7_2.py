''' Reversing a string '''

def rev():
    s=input('Enter a string: ')
    r=''
    x=list(s)
    l=x[::-1]
    for j in l:
        r+=j
    print('Reversed string: ',r)
rev()
