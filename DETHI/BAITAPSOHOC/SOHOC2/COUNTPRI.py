import sys
def san():
    a=[1]*int(1e6)
    a[0]=a[1]=0
    for i in range(2,int(1e6)):
        if a[i]:
            for j in range(i*i,int(1e6),i):
                a[j]=0
    return a
def dem():
    a=san()
    for i in range(0,int(1e6)):
        a[i]=a[i-1]+a[i]
    return a
a=dem()
n = int(input())
for i in range(3):
    x,y=map(int,input().split())
    print(a[y]-a[x-1])
    print(a[x],a[y],end=' ')
