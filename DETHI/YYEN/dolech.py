from collections import defaultdict as khanh
f = khanh(int)
n = int(input())
a = list(map(int,input().split()))

for i in a:
    f[i]+=1

mi,ma = min(f),max(f)
print(ma-mi,f[ma]*f[mi],end = ' ')