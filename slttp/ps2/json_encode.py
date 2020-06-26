import json

n=int(input())
l=list()
for i in range(n):
    l.append(input().split(','))

d=dict()
for i in l:
    d.update({i[0]:i[1]})

print(json.dumps(d, sort_keys=True))