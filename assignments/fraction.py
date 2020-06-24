
def find_fraction(a):
    a=a.split('/')
    if len(a)==1:
        return float(a[0])
    else:
        return float(float(a[0])/float(a[1]))

lst=input().split(' ')
one = find_fraction(lst[0])
two = find_fraction(lst[1])

d={'add':round(one+two,5), 'sub': round(one-two,5), 'mul': round(one*two,5), 'div': round(one/two,5), '==': round(one,5)==round(two,5), '<': one<two, '>': one>two,'<=': one<=two,'>=': one>=two,'!=': one!=two , 'abs_1': abs(one), 'abs_2': abs(two), 'abs eql': round(abs(one),5)==round(abs(two))}

for k,v in d.items():
    print(k + ':' + str(v))