from bisect import bisect_left

n, k = map(int, input().split())
a, b = [0], [0]
for i in range(n):
    a.append(int(input()))
a.sort()
d = 0
print(a)
for i in range(1, n + 1):
    idx = bisect_left(a, a[i] + k) - 1
    if (idx <= n) and (abs(a[idx] - a[i]) <= k) and (i != idx):
        d += 1
        print("y")
    print(i, idx)

print(d)
"""
6 5
25 
50 
50
10
20
23

"""
