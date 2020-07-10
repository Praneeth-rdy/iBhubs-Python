n=int(input())
a=[]
for i in range(n):
    a.append(input().split(','))

a.sort(key=lambda x : (int(x[1]),int(x[2]),int(x[3]),[-ord(c) for c in x[0]]),reverse=True)

for i in range(3):
    print('+',end='')
    for j in range(25):
        print('-',end='')
        if(j==24):
            print('+',end='')
    for k in range(3):
         print('----+',end='')
         if(k==2):
             print()
    if(i==0):
        print('| {:23} |  D |  G |  S |'.format("Merchant"))
    if(i==1):
        for l in range(n):
            print('| {name:<23} | {m:>2} | {p:>2} | {c:>2} |'.format(name=a[l][0],m=a[l][1],p=a[l][2],c=a[l][3]))
            