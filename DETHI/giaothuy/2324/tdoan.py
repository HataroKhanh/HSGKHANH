import bisect
f = {}
n,k = map(int,input().split())
a = [0]+list(map(int,input().split()))
b = [0]
dmin = float('inf')
for i in range(1,n+1):
    b.append(a[i] + b[i-1])
for i in range(1,n+1):
    idx = bisect.bisect_left(b,b[i-1]+k)
    if  idx<n+1 and b[idx]-b[i-1]==k:
        dmin = min(dmin,idx-i+1)
        f[dmin] = i
print(f[dmin],dmin)