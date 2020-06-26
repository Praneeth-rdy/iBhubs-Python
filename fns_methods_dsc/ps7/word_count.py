words=input().lower().split(' ')

s=set(words)
s=list(s)
d={}

for i in s:
    count=0
    for j in words:
        if i==j:
            count+=1
    d.update({i:count})

words=[[i,j] for i,j in d.items()]
words=sorted(words, key=lambda x: (-x[1],x[0]))
for i in words:
    print(i[0], i[1], sep=',')