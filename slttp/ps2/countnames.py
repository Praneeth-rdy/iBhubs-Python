from collections import Counter
names=input().split(' ')

names=[i.capitalize() for i in names]

value_counts=Counter(names)
l=value_counts.most_common()

l=sorted(l, key=lambda x:x[0])

print(l)