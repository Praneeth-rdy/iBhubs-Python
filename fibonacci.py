n=int(input())

def fn(n):
    if n==1 or n==2:
        return 1
    else:
        return fn(n-1)+fn(n-2)

if n!=0:
    for i in range(n):
        print(fn(i+1),end='')
    print()