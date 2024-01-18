s = input()
n = len(s)
smax = 1
for i in range(n):
    l, r = i - 1, i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    k = r - l - 1
    smax = max(smax, k)

print(smax if n%2!=0 else smax+1)
