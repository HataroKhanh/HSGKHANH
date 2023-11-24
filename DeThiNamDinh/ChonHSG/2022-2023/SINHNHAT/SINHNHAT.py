import sys
from collections import defaultdict
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=sorted(a,reverse=True)
ab=defaultdict(lambda:0)

if n>k:
    ssum=0
    for i in range(k):
        ssum+=b[i]
        ab[b[i]]+=1
    print(ssum)
    for i in range(n):
        if ab[a[i]]>=1:
            print(i+1,end=" ")
else:
    print(sum(a))
    for i in range(n):
            print(i+1,end=" ")




