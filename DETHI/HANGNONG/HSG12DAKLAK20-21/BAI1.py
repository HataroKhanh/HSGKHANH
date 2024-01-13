n = int(input())
a = []
for i in range(n):
    ip = list(map(int,input().split()))
    a.append(ip)
def khanh(a,i,j,n):
    sx,sy=0,0
    for d in range(0,n):
        sx+=a[i][d]
        sy+=a[d][j]
    return sx==sy   
d=0
for i in range(n):
    for j in range(n):
        if khanh(a,i,j,n):
            d+=1
print(d)
        