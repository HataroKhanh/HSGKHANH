f = {0: 0}
n, k = map(int, input().split())

a = [0] + list(map(int, input().split()))
ssum = 0
sdem = 0

for i in range(1, n + 1):
    ssum += a[i]
    if ssum % k == 0:
        sdem += 1

    if (ssum - k) in f:
        sdem += f[ssum - k]

    if ssum in f:
        f[ssum] += 1
    else:
        f[ssum] = 1

print(sdem)