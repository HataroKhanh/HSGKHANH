from collections import defaultdict


def san(x, y):
    n = y - x
    c = [[] for _ in range(n + 2)]

    for i in range(x, (int(y**0.5)) + 1):
        for j in range(i * i, y + 1, i):
            c[j].append(i)
            if i * i != j:
                c[j].append(j // i)
    return c


f = defaultdict(lambda: 0)
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    f[i] = i
x, y = map(int, input().split())
c = san(x, y + 1)


ssum = 0
for i in range(x, y + 1):
    d = 0
    ck = 0
    for j in c[i]:
        if f[j]:
            d += 1
        if d >= k:
            ck = 1
            break
    if ck:
        ssum += 1
print(ssum)
