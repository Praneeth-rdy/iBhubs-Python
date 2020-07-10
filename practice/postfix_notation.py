#Enter the post fix notation separating numbers and operands with a space

def operation(op1,op2,op):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2
    else:
        return op1/op2

expression=input().split(' ')

l=[]

for i in expression:
    if i not in ['+','-','*','/']:
        l.append(float(i))
    else:
        b=l.pop()
        a=l.pop()
        l.append(operation(a,b,i))

print(int(l[0]))
        