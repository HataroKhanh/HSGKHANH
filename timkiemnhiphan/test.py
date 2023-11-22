n=int(input())
a=[1,3,2,3]
aa=[1,4,6,9]
print(a)
print(aa)
from collections import defaultdict
f=defaultdict(lambda:0)
for i in a:
    f[i]+=1
    print(dict(f))


