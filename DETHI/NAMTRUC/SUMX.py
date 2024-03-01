from collections import defaultdict as bui
f = bui(lambda:0)
n,k = map(int,input().split())
a = list(map(int,input().split()))
d = 0
for i in range(n):
    if k-a[i] in f:
        d+=f[k-a[i]]
    f[a[i]]+=1
print(d)