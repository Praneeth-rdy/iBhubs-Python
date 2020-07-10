n=int(input())#n<=3000

def thousands(a): #0<=a<=9
    return 'M'*a

def hundreds(a):
    if a<=3:
        return 'C'*a
    elif a<=5:
        return (5-a)*'C'+'D'
    elif a<=8:
        return 'D'+(a-5)*'C'
    else:
        return 'CM'

def tens(a):
    if a<=3:
        return 'X'*a
    elif a<=5:
        return (5-a)*'X'+'L'
    elif a<=8:
        return 'L'+(a-5)*'X'
    else:
        return 'XC'

def ones(a):
    if a<=3:
        return 'I'*a
    elif a<=5:
        return (5-a)*'I'+'V'
    elif a<=8:
        return 'V'+(a-5)*'I'
    else:
        return 'IX'

l=[]
count=0
while count!=4:
    l.append(n%10)
    n=n//10
    count +=1

print(thousands(l[3])+hundreds(l[2])+tens(l[1])+ones(l[0]))