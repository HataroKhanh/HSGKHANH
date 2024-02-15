from bisect import bisect_right

dmin = float('inf')
n,k = map(int,input().split())
a = [0] + list(map(int,input().split()))
b = [0]

for i in range(1,n+1):
	b.append(a[i]+b[i-1])
print(b)
for i in range(n+1):
    db = bisect_right(b,k+a[i])
    if db-1<n+1 and b[db]-b[i-1]==k:
        dmin = min(dmin,db - i+1)
print(dmin)
