from collections import defaultdict

f = defaultdict(lambda:0)
n = int(input())
a = []
for i in range(n):
    f[input()]+=1
dmax = max(f.values())
b = sorted(f.keys(),key = lambda x:int(x))
for i in b:
    if f[i]==dmax:
        print(i)
    

