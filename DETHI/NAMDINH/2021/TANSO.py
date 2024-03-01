from collections import defaultdict

f = defaultdict(lambda: 0)
n = int(input())
a = []
for i in range(n):
    ip = int(input())
    if ip not in a:
        a.append(ip)
    f[ip] += 1

for i in a:
    print(i, f[i])
