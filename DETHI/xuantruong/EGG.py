k, n = map(int, input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
a = sorted(a, key=lambda x: x[0])
s = 0
for i in a:
    if i[1] <= k:
        k -= i[1]
        s += i[0] * i[1]
    elif i[1] > k:
        s += i[0] * k
        break
print(s)
