def khanh(a,n,k,m):
    s = 0
    d = 0
    for i in range(n):
        s+=a[i]
        if s==m:d+=1
        elif s>m:
            d+=1
            i=i-1
    print(m,d,k)
    return d<=k
            
n,k = map(int,input().split())
a = []

mid= 0
l,r = float('inf'),n
for i in range(n):
    ip = int(input())
    l = min(l,ip)
    a.append(ip)
while l <= r:
    mid = (l + r) // 2
    ck  = khanh(a, n, k, mid)
    if ck:
        r = mid - 1
    else:
        l = mid + 1
print(mid)