def is_pal(s):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return is_pal(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_pal(a)==True):
    print("String is a palindrome!")
else:
    print("String is not a palindrome!")
