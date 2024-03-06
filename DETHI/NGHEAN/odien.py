from sys import stdin,stdout



stdin = open("odien.inp","r")
stdout = open("odien.out","w")
n,k = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)

if k == 1:
    print(0)
else:
    i = 0
    d = 0
    while k!=0:
        if i>=n:
            d = -1
            break
        if k<=a[i]:
            d+=1
            break
        else:
            d+=1
            k-=a[i]-1
            i+=1 
    print(d)
