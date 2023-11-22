from itertools import combinations
from collections import defaultdict
a=defaultdict(lambda:0)
dung=['H','S','G','P','T']
n=int(input())
for i in range(n):
    k=input()
    if k[0] in dung:
        a[f"{k[0]}"]+=1
b=0
a=a.values()
# print(list(combinations(a,3)))
for i in combinations(a,3):
    b+=i[0]*i[1]*i[2]
print(b)
