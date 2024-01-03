def Mmax(a,d,n,m):
    s=0
    i=0
    for j in range(0,n):
        s+=a[i]
        if s>d:
            if (j-i)>m:
                i=j
            else:pass

        
n,m=map(int,input().split())
a=[0,]
for i in range(n):  
    ip=int(input())
    a.append(ip)
s=0
for i in range(0,n):
    s+=a[i]
    print(s,end=' ')    




