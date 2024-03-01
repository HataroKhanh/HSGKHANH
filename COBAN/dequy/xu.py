def khanh(a,n,k):
    a = [0]+a
    ssum1,ssum2 = 0,0
    t = k//10
    smax = 0
    if n%k==0:
        for i in range(1,n+1,k):
            ssum+=sum(a[i:k+i])-min(a[i:k+i])
    else:
        i,j = 1,k
        dmin = float('inf')
        while j<=n:
            dmin = min(a[i:j])
            i+=k,j+=k
        while j<=n:
            if min(a[i:j])
            i+=k,j+=k
        
            
            
    
        
n = int(input())
a = list(map(int,input().split()))
i,j = 1,n
mid = 0
temp = sum(a)
print(temp)
while i<=j:
    mid = (i+j)//2
    kq=khanh(a,n,mid)
    print(kq)
    if kq>temp:
        j = mid-1
        temp = kq
    elif kq<=temp:
        i = mid+1
print(mid)
    