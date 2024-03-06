from bisect import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
d = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        idx = bisect(a,-(a[i]-a[j]))
        if (idx-1<n) and (-(a[i]-a[j]) == a[idx-1]) and ((a[i]!=a[idx-1]) and (a[j]!=a[idx-1])):
            d+=1
            print(a[i],a[j],a[idx-1])
print(d)

