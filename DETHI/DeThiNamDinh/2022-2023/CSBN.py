from math import comb
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
d = 0
for i in b.values():
  d+=comb(i,2)
print(d)

