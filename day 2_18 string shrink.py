s="geeks"
print(s)
for i in range (len(s)-1):
    s=s.replace(s[i],".")
    i=i-1
    print(s)
