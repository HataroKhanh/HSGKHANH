n,k = map(int,input().split())
a = list(map(int,input().split()))+[0]

b = [0]*(n+1)
for i in range(n-1,-1,-1):
    b[i]=max(b[i+1],a[i])
d = 0
for i in range(0,n):
    d+=b[i]-a[i]
print(d)

