import sys
#sys.stdin = open("tm.INP","r")
#sys.stdout = open("TM.OUT","w")

n,k = map(int,input().split())
a = list(map(int,input().split()))

a = sorted(a)
a = reversed(a)
kq = 0
if n%2==0:
    for i in range(1,n):
        kq+=a[i]+a[i-1]
    kq+=1
else:
    for i in range(2,n):
        kq+=a[i]+a[i-1]
    kq+=a[0]-1
print(kq)
        
