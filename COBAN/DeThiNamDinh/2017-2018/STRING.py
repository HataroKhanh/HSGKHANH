s=input().split(' ')
from collections import defaultdict
a=defaultdict(lambda:0)
for i in s:
    a[i]+=1;
smax=max(a)
print(smax)
for i in a.items():
    # print("khanh")
    if (smax==i[1]):
        print(i[0])
        break;

