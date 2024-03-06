#ShenYun
import sys
from math import lcm
n,a,b = map(int,input().split())
c = lcm(a,b)
d = 0
i = 1
while c<=n:
    c*=i
    i+=1
    d+=1
print(d)