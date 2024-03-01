import sys
smax = int(1e6)
a = [1]*smax
a[0]=a[1]=0
for i in range(2,int(smax*0.5)+1):
    for j in range(i*i,smax,i):
        a[j]=0
n = int(input())
for i in range(2,n//2+1):
    if a[i] == 1 and a[n-i]==1:
        print(i,n-i)
        sys.exit(0)
print(-1)

