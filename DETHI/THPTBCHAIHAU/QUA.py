from collections import  defaultdict
f = defaultdict(list)
n = int(input())
a = []
for i in range(n):
    x,y = map(int,input().split())
    a.append([x,y])
smax = 0
for i in range(n):
    temp = a[i][0]
    ssum = 0
    for j in range(i,n):
        if temp>a[j][0]:
            temp = a[j][0]
            ssum+=a[j][1]
    smax=max(smax,ssum)
print(smax)
            