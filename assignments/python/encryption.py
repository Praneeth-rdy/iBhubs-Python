
def list_to_string(s):
    str1 = ""
    for ele in s:  
        str1 += str(ele)
    return str1

def binary(a):
    l1=[]
    while a!=0:
        l2=[]
        l2.append(a%2)
        l1=l2+l1
        a=a//2
    return int(list_to_string(l1))

def add_consecutive_ones(a):
    i=0
    a=str(a)
    a=[i for i in a]
    while i<len(a):
        if a[i]=='1':
            count=0
            j=i
            while a[i]=='1':
                i+=1
                if i==len(a):
                    break
            count=i-j
            a[j:i]=[str(count)]
            i=j+1
        else:
            i+=1
    return list_to_string(a)




word = input().strip()

word = [ord(char)-96 for char in word]

r = [num%9 for num in word]
q = [num//9 for num in word]


rs=qs=''
for i,j in zip(r,q):
    rs+=str(i)
    qs+=str(j)

r=int(rs)
q=int(qs)

r=add_consecutive_ones(binary(r))
q=add_consecutive_ones(binary(q))

print('({}, {})'.format(r,q))

