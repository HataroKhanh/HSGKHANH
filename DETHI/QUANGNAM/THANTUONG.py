from collections import defaultdict
n = int(input())
f = defaultdict(lambda:0)
for i in range(n):
    f[input()]+=1
fsort = sorted(f.keys())
smax = -1
for i in f.items():
    smax = max(smax,i[1])
for i in fsort:
    if f[i] == smax:
        print(i)