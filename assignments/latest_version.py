k=input()
l=input()
v=k.split('.')
s=l.split('.')
i=0
if len(v)<=len(s):
    while i<len(v):
        if int(v[i])>int(s[i]):
            print(k)
            break
        elif int(v[i])<int(s[i]):
            print(l)
            break
        else:
            i+=1
else:
    while i<len(s):
        if int(s[i])>int(v[i]):
            print(l)
            break
        elif int(s[i])<int(k[i]):
            print(k)
            break
        else:
            i+=1
    