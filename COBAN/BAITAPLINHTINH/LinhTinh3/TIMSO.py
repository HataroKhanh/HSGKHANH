from bisect import bisect_left
def tongtt(a,n,k):
    i,j=0,k
    smax = 0
    while j<n:
        ssum = sum(a[i:j])
        smax=max(smax,ssum)
        i+=1;j+=1
    return smax
    
n,k = map(int,input().split())
a = [int(i) for i in input().split()]
print(a[bisect_left(a,k)])
print(tongtt(a,n,k))
