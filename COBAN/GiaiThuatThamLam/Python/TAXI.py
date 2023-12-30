from collections import defaultdict
n = int(input())
a=[int(i) for i in input().split()]

f = defaultdict(lambda:0)

for i in a:
    f[f"{i}"] += 1 
print(f)


