n = input()

array = [int(i) for i in input().strip().split(' ')]

array = sorted(array, key=lambda x:x)

m = list()
m=[abs(array[1]-array[0]), (array[0], array[1])]
for i in range(1, len(array)-1):
    d = abs(array[i+1] - array[i])
    if m[0] > d:
        m = [d , (array[i], array[i+1])]
    if m[0] == d:
        m.append((array[i], array[i+1]))

m.pop(0)
m=list(set(m))
m=sorted(m, key=lambda x:x[0])
for i in m:
    print(i[0], i[1])