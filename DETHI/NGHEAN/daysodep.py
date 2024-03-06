from collections import defaultdict

f = defaultdict(lambda:0)
n,k  =map(int,input().split())
a = list(map(int,input().split()))
b = []
i=0
for j  in range(n):
    b.append(-1 if a[j]&1==1 else 1)
print(b)
i = 0
ssum = 0
l = 0
for j in range(n):
    if l >= 1: 
        ssum+=b[j]
        if ssum>=0:pass
        