n = int(input())
a = [int(i) for i in input().split()]
b = [0]
for i in range(1,n+1):
    b.append(b[i-1]+a[i])
smax,lmax=0,0
for i in range(0,n,2):
    lmax+=sum(a)