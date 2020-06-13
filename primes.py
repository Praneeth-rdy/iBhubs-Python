#first line contains number 't' upto which prime numbers are to be printed.

from math import sqrt

def isprime(a):
    k=2
    while k<=sqrt(a):
        if a%k==0:
            return 0
        k+=1
    return 1
            
def primes(n):
    l=[]
    for i in range(n-1):
        if isprime(i+2)==1:
            l.append(str(i+2))
    l=' '.join(l)
    print(l)

t=int(input())
primes(t)