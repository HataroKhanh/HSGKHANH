n,q = map(int,input().split())
ql = [int(i) for i in input().split()]
ql.insert(0,0)
qsum = [0]*(n+1)
for i in range(1,n+1):
    qsum[i] = qsum[i-1]+ql[i]
for i in range(n):
    x,y = map(int,input().split())
    print(qsum[y]-qsum[x-1])