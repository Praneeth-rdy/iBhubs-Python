def compute_fib(n):
    global d
    if n in d.keys():
        return d[n]
    else:
        d[n]=fib(n)
        return compute_fib(n)

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input())
l=[]
for i in range(n):
    l.append(int(input()))
d={}
for i in l:
    print(compute_fib(i))
