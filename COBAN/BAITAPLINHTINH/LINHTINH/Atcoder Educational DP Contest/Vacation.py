n = int(input())
a = []

for i in range(n):
    a.append(list(map(int,input().split())))
a.append([0,0,0])
A,B,C = True,True,True
ssum = 0
for i in range(n):
    smax = max(a[i])
    if smax == a[i][0]:
        ssum+=smax
        a[i+1][0]=0
    elif smax == a[i][1]:
        ssum+=smax
        a[i+1][1]=0
    elif smax == a[i][2]:
        ssum+=smax
        a[i+1][2]=0
print(ssum)

