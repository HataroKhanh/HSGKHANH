import sys
sys.stdin = open("TM .INP","r")
sys.stdout = open("TM.OUT","w")
n,k = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
kq = 0
for i in range(n-1,-1,-k):
    kq+=(a[i]-1)*2
print(kq)
        
