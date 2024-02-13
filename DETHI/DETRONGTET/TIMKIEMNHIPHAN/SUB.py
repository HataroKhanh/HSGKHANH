from bisect import bisect_right
n,k = map(int,input().split())
a = [0]+ list(map(int,input().split()))
b = [0]
for i in range(1,n+1):
    b.append(a[i]+b[i-1])
dmax = float('inf')
for i in range(1,n+1):
    ix = bisect_right(b,k+b[i-1])
    print(ix)
    if ix<=n:
        if b[ix]-b[i-1]>=k:
            dmax = min(dmax,ix-i)
        
print(dmax)
#5 1 3 5 10 7 4 9 2 8
