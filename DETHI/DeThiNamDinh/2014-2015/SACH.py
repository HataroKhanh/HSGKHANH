n,k=map(int,input().split())
a=[int(i) for i in input().split()]

i=0;j=0
d=0;smax=0
for j in range(n):
    d+=a[j]
    if d>k:
        d-=a[i]
        i+=1
        j-=1
    smax=max(smax,j-i+1)
print(smax)
