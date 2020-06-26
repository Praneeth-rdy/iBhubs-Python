from collections import Counter

word=input().lower()
n=int(input())
word=[i for i in word]

value_counts = Counter(word)
word = value_counts.most_common()
word = sorted(word, key=lambda x:(-x[1],x[0]))
l=[]
for i in range(n):
    l.append(word[i])
print(l)