a = [int(i) for i in input().strip().split(' ')]

def Reverse(lst):
    lst.reverse()
    return lst
def smaller(lst, number):
    for i in lst:
        if i < number:
            return i
    return 0
def diff(lst1, lst2, number):
    return abs(smaller(lst1, number) - smaller(lst2, number))
def absdf(lst, index):
    if index == len(lst)-1:
        return diff(Reverse(lst[:index]), [], lst[index])
    else:
        num = lst[index]
        return diff(Reverse(lst[:index]), lst[index+1:], num)

l = list()
for i in range(len(a)):
    l.append(absdf(a, i))

print(max(l))