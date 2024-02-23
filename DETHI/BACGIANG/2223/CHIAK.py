from collections import defaultdict

n, k = map(int, input().split())
f = defaultdict(lambda: 0)
a = list(map(int, input().split()))
s = 0
d = 0

for i in range(n):

    s += a[i]

    if s % k == 0:
        d += 1
    if (s - k)%k in f:
        d += f[(s-k)%k]
    f[s%k] += 1
print(d)


