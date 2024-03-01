n = int(input())
a = [0] + list(map(int, input().split()))

b = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    b[i] = max(a[i], b[i + 1])
smax = 0
for i in range(1, n + 1):
    smax = max(smax, b[i] - a[i])
print(smax)
