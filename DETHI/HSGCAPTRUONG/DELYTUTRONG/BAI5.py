n = int(input())
a=[[0,0]]
for i in range(n):
    x,y = map(int,input().split())
    a.append([x,y])
a = sorted(a, key=lambda x: (int(x[0]), -int(x[1])),reverse=True)

smin=0
for i in range(1,n+1):
   smin+=a[i][0]*(i-1) + a[i][1]*(n-i)
print(smin)   
