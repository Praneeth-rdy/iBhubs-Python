names=input().split(',')

names=sorted(names, key= lambda x: int(x[x.rindex('_')+1:]))

c=1
for name in names:
    if c==len(names):
        print(name)
    else:
        print(name, end=',')
        c+=1