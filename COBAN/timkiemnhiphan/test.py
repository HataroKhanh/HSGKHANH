n, k = map(int, input().split())
a = list(map(int, input().split()))
ssum = float("inf")
for i in range(n):
    d = 0
    for j in range(i, n):
        d = max(d, sum(a[i : j + 1]))
        print(a[i : j + 1])
    print(d)
    ssum = min(ssum, d)
print(ssu