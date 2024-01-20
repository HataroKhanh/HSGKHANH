n = int(input())
k = int(input())
a = [0]+list(map(int, input().split()))
l,r = 1,1
ssum = 0
dmax=0
while r<n:
    ssum += a[r]
    if ssum%k==0:
        dmax = max(dmax,r-l+1)
        if l<r:
            l+=1
        else:r+=1
    else:
        r+=1
        ssum-=a[l]
print(dmax)


