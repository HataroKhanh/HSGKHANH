from collections import defaultdict

f = defaultdict(lambda:0)
n,k = map(int,input().split())
a = []
for i in range(n):
    f[input()]+=1
sdem = 0
d = list(f.keys())
for i in d:
    sdem+=f[i]*f[str(k-int(i))]
print(sdem//2)