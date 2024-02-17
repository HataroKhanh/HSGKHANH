
from collections import defaultdict
k=int(input())
s=input()
n=len(s)
f=defaultdict(lambda : 0)
f[0]=1
b=0
d=0
for i in range(n-1,-1,-1):
    b+=int(s[i])
    if b>=k:
        d+=f[b-k]
    f[b]+=1
print(d)
