from math import comb
from collections import defaultdict
n = int(input())
a = [int(i) for i in input().split()]
f = defaultdict(lambda :0)
for i in a:
    if i%2==0:
        f['chan']+=1
    else:
        f['le']+=1
if sum(a)%2!=0:
    print(comb(n,2)-comb(f['chan'],2)-comb(f['le'],2))
else:
    print(comb(f['chan'],2)+comb(f['le'],2))