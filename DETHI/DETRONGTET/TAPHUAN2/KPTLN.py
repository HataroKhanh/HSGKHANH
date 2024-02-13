n,k = map(int,input().split())
a = [0] + list(map(int,input().split()))
asum = [0]
for i in range(1,n+1):
    asum.append(asum[i-1]+a[i])

i,j = 1,1+k-1
smax = -1
while j<n:
    smax = max(smax,asum[j]-asum[i-1])
    j+=1;i+=1
i,j = 1,1+k-1
while j<n:
    if asum[j]-asum[i-1]==smax:
        print(smax)
        print(' '.join([str(d) for d in range(i+1,j+2)]))
        break
    j+=1;i+=1

#2 3 4 2 3 4 -11 16