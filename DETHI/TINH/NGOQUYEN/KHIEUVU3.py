from bisect import bisect_left
n,k = map(int,input().split())
a=sorted(list(map(int,input().split())))
d=0 
for i in range(n):
    db = bisect_left(a,a[i]+k)
    if db<n:
        if a[db]-a[i]==k:d+=1
print(d)
