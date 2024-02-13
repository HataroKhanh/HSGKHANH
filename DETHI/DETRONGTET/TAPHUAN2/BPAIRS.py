from math import comb
from collections import defaultdict

sdem = 0
f = defaultdict(lambda:0)
n = int(input())
a = list(map(str,input().split()))
b = [int(sum(map(int,i))) for i in a]
for i in b:
    f[str(i)]+=1

for i in f.items():
    sdem+=comb(i[1],2)
print(sdem)