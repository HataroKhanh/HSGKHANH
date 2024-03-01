n = int(input())
a = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = a[i] + a[i - 1]
print(*a[1:])
