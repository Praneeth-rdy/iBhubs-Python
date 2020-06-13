#imports and modules/practice set 3/math module 4

import math

l=[int(i) for i in input().split(',')]
m=l[0]
n=l[1]

p=m**n

if p<1:
     count=0
     while p<1:
         p=p*10
         count -= 1
     fract_part=p-math.floor(p)
     a=math.floor((round(fract_part,4))*100)+count
     print(a)
elif p>=10:
    count=0
    while p>=10:
        p=p/10
        count +=1
    fract_part=p-math.floor(p)
    a=math.floor((round(fract_part,4))*100)+count
    print(a)
else:
     fract_part=p-math.floor(p)
     a=math.floor((round(fract_part,4))*100)
     print(a)
