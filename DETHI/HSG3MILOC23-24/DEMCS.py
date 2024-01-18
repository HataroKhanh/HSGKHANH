from math import log
from bisect import bisect
n = int(input())
a = list(map(int,input().split()))
d=0
pow2 = []
for i in range(32):
    pow2.append(2**i)
for i in a:
    d+=pow2()
    