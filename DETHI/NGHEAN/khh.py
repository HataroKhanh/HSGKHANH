from sys import stdin,stdout


stdin = open("kkh.inp","r")
stdout = open("khh.out","w")

a = [0]*int(1e6)
smax = int(1e6)
for i in range(1,int(smax**0.5)+1):
    for j in range(i*i,smax,i):
        a[j]+=i
        if j!=i*i:            a[j]+=j//i
x,y = map(int,input().split())
d = 0
for i in range(x,y+1):
    if a[i]-i>i:
        d+=1
print(d)
    