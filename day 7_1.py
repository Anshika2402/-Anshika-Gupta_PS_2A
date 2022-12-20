''' Length of a string '''

def lenstr():
    s=input('Enter a string: ')
    c=0
    for i in s:
        c+=1
    print('Length of string: ',c)
lenstr()
