from collections import defaultdict

f = defaultdict(lambda:0)

n = int(input())
a = []
dmin,dmax =float('inf'),0
for i in range(n):
	x,y  = map(int,input().split())
	for i in range(x,y+1):
		f[i]+=1
	dmin = min(x,dmin)
	dmax = max(y,dmax)
	a.append((x,y))
d = max(f.values())
print(d)


 