n, k = map(int, input().split())
a = [int(i) for i in input().split()]
aa = []
for i in range(n):
    kk = 0
    for j in range(i, n):
        kk += a[j]
        if kk == k:
            aa.append([i, j])
            break
ab = max(aa, key=lambda a: a[1]-a[0])
for i in range(ab[0], ab[1]+1):
    print(a[i], end=' ')
