from collections import defaultdict
fi = defaultdict(lambda:0)
n = int(input())
a=[int(i) for i in input().split()]

for i in a:
    fi[f"{i}"]+=1
smax = 0
for i in fi.items():
    smax=max(smax,i[1])
print(smax)
