from math import lcm
import sys
def khanh(a,n):
    b=[0]*(n+1)
    b[0]=a[0]
    b[n]=a[n-1]

    for i in range(1,n):
        b[i]=lcm(a[i-1],a[i])
    b=map(str,b)
    return b 
test = int(input())
for i in range(test):
    n=int(input())
    a=[int(i) for i in input().split()]
    print(' '.join(khanh(a,n)))
    
