from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = []
f = defaultdict(int)
d = 0
for i in a:
    b.append(i%3)
for i in b:
    if i==0:
        d+=f[i]
    elif i==1:
        d+=f[2]
    elif i==2:
        d+=f[1]
    f[i]+=1
print(d)
