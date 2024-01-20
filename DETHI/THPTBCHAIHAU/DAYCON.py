from bisect import bisect_right
from math import comb
n,m = map(int,input().split())
a = [0]+list(map(int,input().split()))
b = [0]
sdem = 0
for i in range(1,n+1):
    b.append(a[i]+b[i-1])
i=1
while i<=n:
    db = bisect_right(b,b[i]+m)
    if db<n:
        if (b[db-1]-b[i-1])<=m:
            sdem+=comb(db-i,2)
        i=db-1
    i+=1
for i in range(1,n+1):
    if a[i]<=10:
        sdem+=1
print(sdem)