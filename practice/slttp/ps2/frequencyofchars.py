from collections import Counter

word=input().lower()
word=[i for i in word]

value_counts = Counter(word)
word = value_counts.most_common()
word = sorted(word, key=lambda x:x[0])
print(word)