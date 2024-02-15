from bisect import bisect_right

dmin = float('inf')
n,k = map(int,input().split())
a = [0] + list(map(int,input().split()))
b = [0]

for i in range(1,n+1):
	b.append(a[i]+b[i-1])

for i in range(1,n+1):
	db = bisect_right(b[1:],k)
	if db<=n:
		if b[db]-b[i-1]==k:
			dmin = min(dmin,db - i)
			print(dmin)
print(db)