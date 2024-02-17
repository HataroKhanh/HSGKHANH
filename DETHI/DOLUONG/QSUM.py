n,k = map(int,input().split())
a = [0] + list(map(int,input().split()))
b = [0]

for i in range(1,n+1):
    b.append(a[i]+b[i-1])
for i in range(k):
    x,y = map(int,input().split())
    print(b[y]-b[x-1])

