from collections import defaultdict as ha

f = ha(lambda: 0)
a = []
n = int(input())
for i in range(n):
    ip = int(input())
    f[ip] += 1
    a.append(ip)
b = []
d = 0
for i in a:
    if f[i] == 1:
        d += 1
        b.append(str(i))
print(d)
print("\n".join(b))
