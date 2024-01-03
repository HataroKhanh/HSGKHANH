N,M = map(int,input().split())
a=[]
for i in range(M):
    x,y = map(int,input().split())
    a.append([x,y])
a=sorted(a,key=lambda x: x[1],reverse=True)
ssum=0
for i in range(M):
    if (a[i][0])<N:
        ssum+=a[i][0]*a[i][1]
        N-=a[i][0]
    else:
        ssum+=N*a[i][1]
        break
print(ssum)

