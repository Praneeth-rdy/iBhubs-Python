m=int(input())

def multiply(term,equation):
    l=[]
    for i in equation:
        l.append([int(term[0])+int(i[0]), int(term[1]) * int(i[1])])
    return l
def multiply_eqn(eqn1, eqn2):
    multiplied=[]
    for term in eqn1:
        multiplied.append(multiply(term, eqn2))
    return multiplied
                
a=[]
for i in range(m):
    a.append(input().split(' '))
n=int(input())
b=[]
for i in range(n):
    b.append(input().split(' '))

final=multiply_eqn(a, b)
equation=[]
for i in final:
    for j in i:
        equation.append(j)
equation.sort(key=lambda x:x[0], reverse=True)
i=0
while i<len(equation)-1:
    if equation[i][0] == (equation[i+1])[0]:
        equation[i:i+2]=[[equation[i][0], equation[i][1]+equation[i+1][1]]]
    else:
        i+=1

print(str(equation[0][1])+'x^'+str(equation[0][0]), end='')
count=1
for i in equation:
    if count==1:
        count+=1
        continue
    if i[0]==0:
        if i[1]>0:
            print(' + '+str(i[1]), end='')
        else:
            print(' - '+str(abs(i[1])),end='')
    elif i[1]<=0:
        if i[1]<0:
            print(' - '+str(abs(i[1]))+'x^'+str(i[0]), end='')
        else:
            continue
    else:
        print(' + '+str(i[1])+'x^'+str(i[0]), end='')

