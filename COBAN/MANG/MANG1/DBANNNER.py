def ij(a,index,n):
    l,r = 0,n+1
    for d in range(index,0,-1):
        if a[d]<a[index]:
            l = d
            break
    for d in range(index,n+1):
        if a[d]<a[index]:
            r = d
            break
    return (r-l-1)*a[index]

n = int(input())
a = [int(i) for i in input().split()]
a.insert(0,0)
ij(a,1,n)
smax = -1
for i in range(1,n+1):
    smax = max(smax,ij(a,i,n))
print(smax)
 